#!/usr/bin/env python3
"""
buckets.py

Multi-URL diagnostic: dispatch one or more test URLs (and a baseline URL)
through ./manage.sh's parse pipeline, bucket each parser's output per
component, and emit a structured JSON report with an aggregated disagreement
metric per component.

By default the metric is baseline-relative: parsers naturally disagree on
benign things even for a clean URL, so only differentials *introduced* by the
test inputs count. With multiple test URLs, the numerator is the **superset**
(union) of pairs that newly differ on any test URL.

Pipeline:
    1. kubectl-exec the manager pod once per URL to enqueue a Celery job and
       capture the job_id. Baseline + every test URL are dispatched up front
       so workers run them in parallel.
    2. Spawn kubectl port-forward for postgres, connect with psycopg2.
    3. Poll each job to completion, fetch parse_results joined with libraries.
    4. Classify each (library, component) cell as 'value' | 'error' | 'exclude'.
    5. For each component C:
         eligible_libs = libs that are non-exclude in the baseline AND in
                         every test run (intersection)
         For each pair (A, B) of eligible_libs:
             baseline_differ  = bucket keys differ on baseline
             test_differ[U]   = bucket keys differ on test URL U
             new_diff[U]      = test_differ[U] AND NOT baseline_differ
             new_diff_union   = OR_{U} new_diff[U]
         Metric:
             eligible_pairs       = C(|eligible_libs|, 2)
             new_diff_pairs_union = # of pairs where new_diff_union is true
             ratio                = new_diff_pairs_union / eligible_pairs
    6. Write JSON (includes per-URL breakdown and pair attribution) and print
       the ratio table to stdout.

With --no-baseline, the metric becomes "pairs that ever differ on any test URL
/ eligible_pairs" — same shape, no baseline subtraction.

Both EXCLUDE rows and parser errors are listed in the buckets section for
visibility but excluded from eligible/mismatch counts. If a library errors on
the baseline or any test URL, it is dropped from the eligible set for that
component entirely (intersection semantics).
"""

import argparse
import atexit
import json
import os
import signal
import socket
import subprocess
import sys
import time
from collections import defaultdict
from math import comb

import psycopg2

COMPONENTS = (
    "scheme", "authority", "userinfo", "username", "password",
    "host", "port", "path", "query", "query_dict", "fragment",
)
EXCLUDE_MARKER = "EXCLUDE"
DEFAULT_BASELINE_URL = "http://sub.example.com/a/b/c?a=b&c=d#frag"

DISPATCH_CODE = (
    "import sys\n"
    "from tasks.parse_url import parse_url\n"
    "r = parse_url.delay(sys.argv[1]).get(timeout=10)\n"
    "print(r['job_id'])\n"
)


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", file=sys.stderr, flush=True)


def parse_args():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("urls", nargs="*", help="one or more URLs to test")
    p.add_argument("--urls-file", default=None,
                   help="path to a file of test URLs, one per line (# comments allowed)")
    p.add_argument("--out", default="buckets.json", help="output JSON path")
    p.add_argument("--baseline-url", default=DEFAULT_BASELINE_URL,
                   help="baseline URL used to establish 'background' disagreements")
    p.add_argument("--no-baseline", action="store_true",
                   help="skip the baseline run; numerator becomes pairs that ever differ "
                        "on any test URL")
    p.add_argument("--namespace", default=os.environ.get("NAMESPACE", "url-parser-fuzzing"))
    p.add_argument("--timeout", type=float, default=30.0,
                   help="seconds to wait for the job to complete")
    p.add_argument("--poll-interval", type=float, default=0.2)
    p.add_argument("--pg-host", default=os.environ.get("PGHOST", "localhost"))
    p.add_argument("--pg-port", type=int, default=int(os.environ.get("PGPORT", "15432")),
                   help="local port for the postgres port-forward")
    p.add_argument("--pg-user", default=os.environ.get("PGUSER", "parser"))
    p.add_argument("--pg-password", default=os.environ.get("PGPASSWORD", "PLACEHOLDER_CHANGE_BEFORE_REPRO"))
    p.add_argument("--pg-db", default=os.environ.get("PGDATABASE", "url_parser"))
    p.add_argument("--no-port-forward", action="store_true",
                   help="assume postgres is already reachable on --pg-host:--pg-port")
    return p.parse_args()


def get_manager_pod(namespace):
    out = subprocess.run(
        ["kubectl", "get", "pods", "-n", namespace,
         "--selector=app=manager",
         "-o", "jsonpath={.items[0].metadata.name}"],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    if not out:
        raise RuntimeError(f"no manager pod found in namespace {namespace}")
    return out


def dispatch_job(namespace, pod, url):
    """kubectl-exec a one-liner that prints just the new job_id."""
    proc = subprocess.run(
        ["kubectl", "exec", "-n", namespace, pod, "--",
         "python", "-c", DISPATCH_CODE, url],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"dispatch failed (rc={proc.returncode}):\nstdout: {proc.stdout}\nstderr: {proc.stderr}"
        )
    line = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else ""
    try:
        return int(line)
    except ValueError:
        raise RuntimeError(f"could not parse job_id from dispatch output: {proc.stdout!r}")


def start_port_forward(namespace, local_port):
    """Spawn kubectl port-forward for svc/postgres on local_port; wait until reachable."""
    pf = subprocess.Popen(
        ["kubectl", "port-forward", "-n", namespace,
         "svc/postgres", f"{local_port}:5432"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        # New process group so we can clean it up without affecting our shell.
        preexec_fn=os.setsid if hasattr(os, "setsid") else None,
    )

    def _cleanup():
        if pf.poll() is None:
            try:
                if hasattr(os, "killpg"):
                    os.killpg(os.getpgid(pf.pid), signal.SIGTERM)
                else:
                    pf.terminate()
            except ProcessLookupError:
                pass
    atexit.register(_cleanup)

    # Wait until the local port accepts connections.
    deadline = time.time() + 10.0
    while time.time() < deadline:
        if pf.poll() is not None:
            raise RuntimeError("kubectl port-forward exited before becoming ready")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                s.connect(("127.0.0.1", local_port))
                return pf
            except OSError:
                time.sleep(0.1)
    raise RuntimeError(f"port-forward to local port {local_port} never became ready")


def wait_for_job(conn, job_id, timeout, poll_interval):
    """Poll parse_jobs.status until 'completed', or until libraries_completed == libraries_total."""
    deadline = time.time() + timeout
    last = None
    with conn.cursor() as cur:
        while time.time() < deadline:
            cur.execute(
                "SELECT status, libraries_completed, libraries_total "
                "FROM parse_jobs WHERE id = %s",
                (job_id,),
            )
            row = cur.fetchone()
            if row is None:
                raise RuntimeError(f"job {job_id} not found")
            status, done, total = row
            if (status, done, total) != last:
                log(f"  job {job_id}: status={status} {done}/{total}")
                last = (status, done, total)
            if status == "completed":
                return
            if total and done >= total:
                return
            time.sleep(poll_interval)
    raise TimeoutError(f"job {job_id} did not complete within {timeout}s (last={last})")


def fetch_results(conn, job_id):
    sql = f"""
        SELECT l.id, l.name, pr.success, pr.error_message,
               {", ".join("pr." + c for c in COMPONENTS)}
        FROM parse_results pr
        JOIN libraries l ON l.id = pr.library_id
        WHERE pr.job_id = %s AND l.enabled = TRUE
        ORDER BY l.name
    """
    with conn.cursor() as cur:
        cur.execute(sql, (job_id,))
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, row)) for row in cur.fetchall()]


def classify(component, raw_value, success, error_message):
    """
    Return (kind, normalized_value, display_value).

      kind            : 'value' | 'error' | 'exclude'
      normalized_value: hashable key used to bucket
      display_value   : the value to render in JSON
    """
    if not success:
        return ("error", ("__error__", error_message or ""), None)

    # query_dict is JSON; the EXCLUDE marker is stored as a JSON string "EXCLUDE".
    if component == "query_dict":
        if raw_value is None:
            return ("value", ("__null__",), None)
        # raw_value is already a Python object (psycopg2 decodes JSON).
        if isinstance(raw_value, str) and raw_value.strip('"') == EXCLUDE_MARKER:
            return ("exclude", ("__exclude__",), EXCLUDE_MARKER)
        # Normalize dicts to canonical JSON for grouping.
        try:
            normalized = json.dumps(raw_value, sort_keys=True, ensure_ascii=False)
        except TypeError:
            normalized = repr(raw_value)
        return ("value", ("v", normalized), raw_value)

    if raw_value == EXCLUDE_MARKER:
        return ("exclude", ("__exclude__",), EXCLUDE_MARKER)
    if raw_value is None:
        return ("value", ("__null__",), None)
    return ("value", ("v", raw_value), raw_value)


def classify_run(rows):
    """
    For one run, build per-component classifications keyed by library_id.

    Returns:
        classifications[component][library_id] = (kind, normalized_key, display_value)
        names[library_id] = library_name
    """
    classifications = {c: {} for c in COMPONENTS}
    names = {}
    for r in rows:
        names[r["id"]] = r["name"]
        for c in COMPONENTS:
            classifications[c][r["id"]] = classify(
                c, r[c], r["success"], r["error_message"]
            )
    return classifications, names


def bucket_summary(classifications_c, names):
    """
    Group library entries for a single component into JSON-friendly buckets.

    classifications_c: dict[library_id] -> (kind, key, display)
    """
    buckets = defaultdict(lambda: {
        "kind": None,
        "value": None,
        "error_message": None,
        "count": 0,
        "library_ids": [],
        "library_names": [],
    })
    for lib_id, (kind, key, display) in classifications_c.items():
        b = buckets[key]
        if b["kind"] is None:
            b["kind"] = kind
            if kind == "value":
                b["value"] = display
            elif kind == "error":
                # The error message is embedded in the key.
                b["error_message"] = key[1] if len(key) > 1 else ""
        b["count"] += 1
        b["library_ids"].append(lib_id)
        b["library_names"].append(names.get(lib_id, str(lib_id)))

    bucket_list = list(buckets.values())
    bucket_list.sort(key=lambda b: (b["kind"] == "exclude", -b["count"]))
    return bucket_list


def aggregate_metric(baseline_c, test_runs_c, names, baseline_mode):
    """
    Aggregate per-pair disagreements across multiple test runs.

    Args:
        baseline_c: dict[lib_id] -> (kind, key, display) for one component
                    on the baseline run, OR None if --no-baseline.
        test_runs_c: list of (url, classifications_c) for each test URL.
        names: dict[lib_id] -> library_name (for human-readable attribution).
        baseline_mode: bool. If False, baseline_c is treated as "everyone agrees"
            so any pair that differs on a test URL counts as new_diff.

    Returns a dict with the aggregated metric plus per-URL counts and a
    pair-level attribution list (which URLs caused each pair to newly differ).
    """
    # eligible libs: produced a successful value on baseline (if any) AND on every
    # test run. Libraries that EXCLUDE or ERROR anywhere are dropped — we don't
    # compare a parser that couldn't return a real value.
    lib_ids = None

    def filter_ids(classifications_c):
        return {i for i, v in classifications_c.items() if v[0] == "value"}

    if baseline_mode:
        lib_ids = filter_ids(baseline_c)
    for _, t_c in test_runs_c:
        present = filter_ids(t_c)
        lib_ids = present if lib_ids is None else (lib_ids & present)
    if lib_ids is None:
        lib_ids = set()
    eligible_ids = sorted(lib_ids)
    eligible = len(eligible_ids)
    eligible_pairs = comb(eligible, 2)

    # Track which libs were dropped from the eligible set and why.
    all_known = set(names)
    if baseline_mode:
        all_known |= set(baseline_c)
    for _, t_c in test_runs_c:
        all_known |= set(t_c)
    dropped = []
    for lid in sorted(all_known - lib_ids):
        reasons = []  # list of {"where": "baseline"|url, "kind": "error"|"exclude", "msg": str|None}
        if baseline_mode and lid in baseline_c and baseline_c[lid][0] != "value":
            kind = baseline_c[lid][0]
            msg = baseline_c[lid][1][1] if kind == "error" and len(baseline_c[lid][1]) > 1 else None
            reasons.append({"where": "baseline", "kind": kind, "msg": msg})
        for url, t_c in test_runs_c:
            if lid in t_c and t_c[lid][0] != "value":
                kind = t_c[lid][0]
                msg = t_c[lid][1][1] if kind == "error" and len(t_c[lid][1]) > 1 else None
                reasons.append({"where": url, "kind": kind, "msg": msg})
        if reasons:
            dropped.append({
                "library_id": lid,
                "library_name": names.get(lid, str(lid)),
                "reasons": reasons,
            })

    # Per-URL stats.
    per_url = []
    for url, _ in test_runs_c:
        per_url.append({
            "url": url,
            "test_diff_pairs": 0,
            "new_diff_pairs": 0,
            "resolved_diff_pairs": 0,
        })

    baseline_diff_pairs = 0
    new_diff_union = 0
    test_diff_union = 0
    pair_attributions = []  # only pairs with non-empty new_diff_urls

    for i in range(eligible):
        a = eligible_ids[i]
        base_a = baseline_c[a][1] if baseline_mode else None
        test_a_keys = [t_c[a][1] for _, t_c in test_runs_c]
        for j in range(i + 1, eligible):
            b = eligible_ids[j]
            base_diff = baseline_mode and (base_a != baseline_c[b][1])
            if base_diff:
                baseline_diff_pairs += 1

            new_urls = []
            any_test_diff = False
            for k, (url, t_c) in enumerate(test_runs_c):
                t_diff = test_a_keys[k] != t_c[b][1]
                if t_diff:
                    per_url[k]["test_diff_pairs"] += 1
                    any_test_diff = True
                if t_diff and not base_diff:
                    per_url[k]["new_diff_pairs"] += 1
                    new_urls.append(url)
                elif base_diff and not t_diff:
                    per_url[k]["resolved_diff_pairs"] += 1

            if any_test_diff:
                test_diff_union += 1
            if new_urls:
                new_diff_union += 1
                pair_attributions.append({
                    "library_a_id": a,
                    "library_b_id": b,
                    "library_a": names.get(a, str(a)),
                    "library_b": names.get(b, str(b)),
                    "urls": new_urls,
                })

    pair_attributions.sort(key=lambda x: (-len(x["urls"]), x["library_a"], x["library_b"]))

    ratio = new_diff_union / eligible_pairs if eligible_pairs else 0.0
    return {
        "eligible": eligible,
        "eligible_pairs": eligible_pairs,
        "baseline_diff_pairs": baseline_diff_pairs,
        "test_diff_pairs_union": test_diff_union,
        "new_diff_pairs_union": new_diff_union,
        "ratio": round(ratio, 6),
        "per_url": per_url,
        "pair_attributions": pair_attributions,
        "dropped_libraries": dropped,
    }


def print_ratio_table(header, components_report, baseline_mode):
    """Emit a fixed-width table of per-component aggregated disagreement ratios."""
    name_w = max(len(c) for c in COMPONENTS)
    if baseline_mode:
        header_cols = ("component", "ratio", "new_diff∪", "base_diff",
                       "test_diff∪", "eligible_pairs", "eligible")
    else:
        header_cols = ("component", "ratio", "diff∪", "(n/a)",
                       "test_diff∪", "eligible_pairs", "eligible")
    widths = (name_w, 8, 9, 9, 11, 14, 8)

    def fmt_row(cols):
        return "  ".join(str(c).ljust(w) for c, w in zip(cols, widths))

    print(f"# {header}")
    print(fmt_row(header_cols))
    print(fmt_row("-" * w for w in widths))
    for c in COMPONENTS:
        r = components_report[c]
        base_col = r["baseline_diff_pairs"] if baseline_mode else "-"
        print(fmt_row((
            c,
            f"{r['ratio']:.4f}",
            r["new_diff_pairs_union"],
            base_col,
            r["test_diff_pairs_union"],
            r["eligible_pairs"],
            r["eligible"],
        )))


def print_per_url_table(components_report, urls):
    """Per-URL breakdown: rows = URLs, columns = per-component new_diff count."""
    if not urls:
        return
    url_w = min(60, max(len(u) for u in urls))
    name_w = max(8, max(len(c) for c in COMPONENTS))
    widths = (url_w,) + tuple(name_w for _ in COMPONENTS)

    def fmt_row(cols):
        return "  ".join(str(c).ljust(w)[:w] for c, w in zip(cols, widths))

    print()
    print("# per-URL new_diff_pairs by component")
    print(fmt_row(("url",) + COMPONENTS))
    print(fmt_row("-" * w for w in widths))
    for k, url in enumerate(urls):
        row = [url]
        for c in COMPONENTS:
            row.append(components_report[c]["per_url"][k]["new_diff_pairs"])
        print(fmt_row(row))


def write_json(path, payload):
    tmp = path + ".partial"
    with open(tmp, "w") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    os.replace(tmp, path)


def read_urls_file(path):
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            out.append(line)
    return out


def main():
    args = parse_args()

    urls = list(args.urls)
    if args.urls_file:
        urls.extend(read_urls_file(args.urls_file))
    if not urls:
        print("error: no test URLs supplied (pass as positional args or --urls-file)",
              file=sys.stderr)
        sys.exit(2)

    baseline_mode = not args.no_baseline

    log(f"locating manager pod in namespace {args.namespace}")
    pod = get_manager_pod(args.namespace)
    log(f"  manager pod: {pod}")

    if baseline_mode:
        log(f"dispatching BASELINE: {args.baseline_url}")
        baseline_job = dispatch_job(args.namespace, pod, args.baseline_url)
        log(f"  baseline job_id={baseline_job}")
    else:
        baseline_job = None

    log(f"dispatching {len(urls)} TEST URL(s)")
    test_jobs = []
    for url in urls:
        job_id = dispatch_job(args.namespace, pod, url)
        test_jobs.append((url, job_id))
        log(f"  {job_id}  {url}")

    if not args.no_port_forward:
        log(f"starting port-forward svc/postgres -> 127.0.0.1:{args.pg_port}")
        start_port_forward(args.namespace, args.pg_port)

    log(f"connecting to postgres at {args.pg_host}:{args.pg_port}/{args.pg_db}")
    conn = psycopg2.connect(
        host=args.pg_host, port=args.pg_port, user=args.pg_user,
        password=args.pg_password, dbname=args.pg_db,
    )
    conn.set_session(readonly=True, autocommit=True)

    try:
        def run_one(label, job_id):
            log(f"waiting for {label} job {job_id} (timeout {args.timeout}s)")
            wait_for_job(conn, job_id, args.timeout, args.poll_interval)
            rows = fetch_results(conn, job_id)
            log(f"  {label} job {job_id}: {len(rows)} library rows")
            return rows

        # Baseline
        baseline_cls = None
        baseline_names = {}
        if baseline_mode:
            base_rows = run_one("baseline", baseline_job)
            baseline_cls, baseline_names = classify_run(base_rows)

        # Tests
        test_runs = []  # list of {url, job_id, classifications, names}
        all_names = dict(baseline_names)
        for url, job_id in test_jobs:
            rows = run_one(f"test[{url}]", job_id)
            cls, names = classify_run(rows)
            all_names.update(names)
            test_runs.append({
                "url": url, "job_id": job_id,
                "classifications": cls, "names": names,
            })

        # Aggregate per component.
        components_report = {}
        for c in COMPONENTS:
            test_runs_c = [(r["url"], r["classifications"][c]) for r in test_runs]
            baseline_c = baseline_cls[c] if baseline_mode else None
            metric = aggregate_metric(baseline_c, test_runs_c, all_names, baseline_mode)
            entry = {**metric}
            if baseline_mode:
                entry["baseline_buckets"] = bucket_summary(baseline_c, all_names)
            entry["test_buckets_per_url"] = [
                {"url": r["url"], "buckets": bucket_summary(r["classifications"][c], all_names)}
                for r in test_runs
            ]
            components_report[c] = entry

        payload = {
            "baseline_url": args.baseline_url if baseline_mode else None,
            "baseline_job_id": baseline_job,
            "test_urls": [{"url": r["url"], "job_id": r["job_id"]} for r in test_runs],
            "libraries": sorted(
                [{"id": lid, "name": n} for lid, n in all_names.items()],
                key=lambda x: x["name"],
            ),
            "components": components_report,
        }

        log(f"writing {args.out}")
        write_json(args.out, payload)
        log("complete")

        if baseline_mode:
            header = (f"baseline={args.baseline_url} (job {baseline_job}) | "
                      f"{len(urls)} test URL(s)")
        else:
            header = f"no baseline | {len(urls)} test URL(s)"
        print_ratio_table(header, components_report, baseline_mode)
        print_per_url_table(components_report, [r["url"] for r in test_runs])
    finally:
        conn.close()


if __name__ == "__main__":
    main()
