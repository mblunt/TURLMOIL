#!/usr/bin/env python3
"""
cluster.py

Interactive REPL for narrowing a set of URL parsers by output clustering.

Loop:
    URL>  enter a URL (or a command)         -> dispatch, fetch, show per-component clusters
    Keep> 'host:1' / 'host:1,3 path:2' / etc -> drop everything outside that selection

Within one component the listed cluster indices are UNIONed (clusters are
disjoint anyway). Across components they are INTERSECTed (libs must be in
each named cluster).

Commands (at either prompt):
    skip                 keep current library set, go on to next URL
    libs                 list current library set
    reset                restore the full library set
    back                 undo the last filter
    quit                 exit

You can seed the first iteration on the CLI:
    python3 cluster.py "https://EXAMPLE.com"
    python3 cluster.py --job-id 1234
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

import psycopg2

COMPONENTS = (
    "scheme", "authority", "userinfo", "username", "password",
    "host", "port", "path", "query", "query_dict", "fragment",
)
EXCLUDE_MARKER = "EXCLUDE"

DISPATCH_CODE = (
    "import sys\n"
    "from tasks.parse_url import parse_url\n"
    "r = parse_url.delay(sys.argv[1]).get(timeout=10)\n"
    "print(r['job_id'])\n"
)


def log(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", file=sys.stderr, flush=True)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("url", nargs="?", help="seed URL for the first iteration")
    p.add_argument("--job-id", type=int, help="seed first iteration from an existing job_id")
    p.add_argument("--libraries", help="comma-separated library names to start with")
    p.add_argument("--namespace", default=os.environ.get("NAMESPACE", "url-parser-fuzzing"))
    p.add_argument("--timeout", type=float, default=30.0)
    p.add_argument("--pg-host", default=os.environ.get("PGHOST", "localhost"))
    p.add_argument("--pg-port", type=int, default=int(os.environ.get("PGPORT", "15432")))
    p.add_argument("--pg-user", default=os.environ.get("PGUSER", "parser"))
    p.add_argument("--pg-password", default=os.environ.get("PGPASSWORD", "PLACEHOLDER_CHANGE_BEFORE_REPRO"))
    p.add_argument("--pg-db", default=os.environ.get("PGDATABASE", "url_parser"))
    p.add_argument("--no-port-forward", action="store_true")
    return p.parse_args()


def get_manager_pod(ns):
    out = subprocess.run(
        ["kubectl", "get", "pods", "-n", ns,
         "--selector=app=manager", "-o", "jsonpath={.items[0].metadata.name}"],
        check=True, capture_output=True, text=True).stdout.strip()
    if not out:
        raise RuntimeError(f"no manager pod in namespace {ns}")
    return out


def dispatch(ns, pod, url):
    p = subprocess.run(
        ["kubectl", "exec", "-n", ns, pod, "--", "python", "-c", DISPATCH_CODE, url],
        capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"dispatch failed (rc={p.returncode}):\n{p.stderr}")
    return int(p.stdout.strip().splitlines()[-1])


def start_port_forward(ns, port):
    pf = subprocess.Popen(
        ["kubectl", "port-forward", "-n", ns, "svc/postgres", f"{port}:5432"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        preexec_fn=os.setsid if hasattr(os, "setsid") else None)

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

    deadline = time.time() + 10
    while time.time() < deadline:
        if pf.poll() is not None:
            raise RuntimeError("port-forward exited before ready")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                s.connect(("127.0.0.1", port))
                return
            except OSError:
                time.sleep(0.1)
    raise RuntimeError("port-forward never became ready")


def wait_for_job(conn, job_id, timeout):
    deadline = time.time() + timeout
    last = None
    with conn.cursor() as cur:
        while time.time() < deadline:
            cur.execute(
                "SELECT status, libraries_completed, libraries_total "
                "FROM parse_jobs WHERE id = %s", (job_id,))
            row = cur.fetchone()
            if row is None:
                raise RuntimeError(f"job {job_id} not found")
            status, done, total = row
            if (status, done, total) != last:
                log(f"  job {job_id}: {status} {done}/{total}")
                last = (status, done, total)
            if status == "completed" or (total and done >= total):
                return
            time.sleep(0.2)
    raise TimeoutError(f"job {job_id} did not complete within {timeout}s")


def fetch_url(conn, job_id):
    with conn.cursor() as cur:
        cur.execute("SELECT url FROM parse_jobs WHERE id = %s", (job_id,))
        row = cur.fetchone()
        return row[0] if row else None


def fetch_results(conn, job_id):
    sql = (
        "SELECT l.id, l.name, pr.success, pr.error_message, "
        + ", ".join("pr." + c for c in COMPONENTS) +
        " FROM parse_results pr JOIN libraries l ON l.id = pr.library_id"
        " WHERE pr.job_id = %s AND l.enabled = TRUE ORDER BY l.name"
    )
    with conn.cursor() as cur:
        cur.execute(sql, (job_id,))
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]


def classify(component, raw, success, err):
    """Return (kind, key, display)."""
    if not success:
        return ("error", ("err", err or ""), err or "")
    if component == "query_dict":
        if raw is None:
            return ("value", ("null",), None)
        if isinstance(raw, str) and raw.strip('"') == EXCLUDE_MARKER:
            return ("exclude", ("excl",), EXCLUDE_MARKER)
        try:
            norm = json.dumps(raw, sort_keys=True, ensure_ascii=False)
        except TypeError:
            norm = repr(raw)
        return ("value", ("v", norm), raw)
    if raw == EXCLUDE_MARKER:
        return ("exclude", ("excl",), EXCLUDE_MARKER)
    if raw is None:
        return ("value", ("null",), None)
    return ("value", ("v", raw), raw)


def cluster_component(rows, component):
    buckets = defaultdict(lambda: {
        "kind": None, "value": None, "error_message": None,
        "count": 0, "library_names": [],
    })
    for r in rows:
        kind, key, disp = classify(component, r[component], r["success"], r["error_message"])
        b = buckets[key]
        if b["kind"] is None:
            b["kind"] = kind
            if kind == "value":
                b["value"] = disp
            elif kind == "error":
                b["error_message"] = disp
        b["count"] += 1
        b["library_names"].append(r["name"])
    for b in buckets.values():
        b["library_names"].sort()
    # exclude buckets last; otherwise descending by count.
    return sorted(buckets.values(), key=lambda b: (b["kind"] == "exclude", -b["count"]))


def render_value(b):
    kind, val, err = b["kind"], b["value"], b["error_message"]
    if kind == "exclude":
        return "<EXCLUDE>"
    if kind == "error":
        return f"<ERROR: {err}>"
    if val is None:
        return "<NULL>"
    if isinstance(val, (dict, list)):
        return json.dumps(val, sort_keys=True, ensure_ascii=False)
    return str(val)


def print_clusters(clusters, components, max_value_w=60, max_libs_w=80):
    for c in components:
        buckets = clusters[c]
        print(f"\n== {c} ==  ({len(buckets)} cluster{'s' if len(buckets) != 1 else ''})")
        for idx, b in enumerate(buckets, start=1):
            v = render_value(b)
            if len(v) > max_value_w:
                v = v[:max_value_w - 3] + "..."
            libs = ", ".join(b["library_names"])
            if len(libs) > max_libs_w:
                libs = libs[:max_libs_w - 3] + "..."
            print(f"  {c}:{idx:<2d}  [{b['count']:2d}]  {v.ljust(max_value_w)}  {libs}")


def fetch_enabled_libraries(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT name FROM libraries WHERE enabled = TRUE ORDER BY name")
        return [r[0] for r in cur.fetchall()]


def parse_filter(spec, clusters):
    """
    Translate a filter string into a set of library names, or a command tag.

    Returns one of:
        ("set",   set_of_library_names)
        ("skip",  None)
        ("reset", None)
        ("back",  None)
        ("quit",  None)
        ("list",  None)

    Filter syntax: whitespace-separated tokens, each shaped 'component:idx[,idx]...'.
    Prefix a token with '-' to *exclude* (drop) those libraries.

        within a token  : cluster indices are UNIONed (1-indexed)
        positive tokens : INTERSECTed -> the include set
        negative tokens : UNIONed     -> the exclude set
        final           : include - exclude

        host:1                keep libs in host's cluster 1
        host:1,3              keep libs in host clusters 1 OR 3
        host:1 path:2         keep libs in host:1 AND path:2
        -host:1               drop libs in host:1, keep everything else
        host:1 -path:2        keep host:1, then drop any also in path:2
        -host:1 -path:2       drop libs in host:1 or path:2
    """
    spec = spec.strip()
    low = spec.lower()
    if not spec or low in ("skip", "s", "keep", "next"):
        return ("skip", None)
    if low in ("quit", "q", "exit"):
        return ("quit", None)
    if low in ("reset", "r"):
        return ("reset", None)
    if low in ("back", "b", "undo", "u"):
        return ("back", None)
    if low in ("libs", "list", "l"):
        return ("list", None)

    include_tokens = []
    exclude_tokens = []
    for token in spec.split():
        negate = token.startswith("-")
        body = token[1:] if negate else token
        if ":" not in body:
            raise ValueError(f"bad token (need 'component:idx'): {token!r}")
        comp, idxs = body.split(":", 1)
        comp = comp.strip()
        if comp not in clusters:
            raise ValueError(f"unknown component: {comp!r}")
        try:
            indices = [int(x) for x in idxs.split(",") if x.strip()]
        except ValueError:
            raise ValueError(f"bad indices for {comp}: {idxs!r}")
        component_clusters = clusters[comp]
        libs_for_token = set()
        for idx in indices:
            if idx < 1 or idx > len(component_clusters):
                raise ValueError(
                    f"{comp}:{idx} out of range (1..{len(component_clusters)})"
                )
            libs_for_token |= set(component_clusters[idx - 1]["library_names"])
        (exclude_tokens if negate else include_tokens).append(libs_for_token)

    if not include_tokens and not exclude_tokens:
        return ("skip", None)

    if include_tokens:
        include = include_tokens[0]
        for s in include_tokens[1:]:
            include &= s
    else:
        # All-negative spec: start from every library in the current view.
        include = set()
        for buckets in clusters.values():
            for b in buckets:
                include |= set(b["library_names"])
            break  # any one component covers every visible lib

    exclude = set()
    for s in exclude_tokens:
        exclude |= s

    return ("set", include - exclude)


def print_help():
    print(
        "\nCommands (case-insensitive):\n"
        "  <URL>                            dispatch URL and show clusters\n"
        "  <component>:<idx>[,<idx>]...     keep libs in those clusters (1-indexed)\n"
        "  -<component>:<idx>[,<idx>]...    drop libs in those clusters\n"
        "  multiple tokens space-separated  positives intersected, negatives unioned\n"
        "  job <id>                         seed from an existing job_id\n"
        "  libs                             show the current library set\n"
        "  reset                            restore the full library set\n"
        "  back                             undo the last filter\n"
        "  skip                             keep current set; just prompt for next URL\n"
        "  help                             this message\n"
        "  quit                             exit\n"
    )


def read_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print()
        return "quit"


class Session:
    """State for the interactive loop."""

    def __init__(self, args, conn, manager_pod):
        self.args = args
        self.conn = conn
        self.pod = manager_pod
        all_libs = fetch_enabled_libraries(conn)
        self.all_libs = set(all_libs)
        if args.libraries:
            initial = {s.strip() for s in args.libraries.split(",") if s.strip()}
            unknown = initial - self.all_libs
            if unknown:
                log(f"warning: unknown libraries in --libraries: {sorted(unknown)}")
            initial &= self.all_libs
        else:
            initial = set(self.all_libs)
        self.history = [initial]
        self.last_clusters = None

    @property
    def current_libs(self):
        return self.history[-1]

    def push(self, libs):
        self.history.append(set(libs))

    def reset(self):
        self.history = [set(self.all_libs)]
        print(f"reset to {len(self.current_libs)} libraries")

    def back(self):
        if len(self.history) > 1:
            self.history.pop()
            print(f"reverted to {len(self.current_libs)} libraries")
        else:
            print("nothing to undo")

    def list_libs(self):
        libs = sorted(self.current_libs)
        print(f"current ({len(libs)}/{len(self.all_libs)}): {', '.join(libs)}")

    # ------- dispatch / cluster -------

    def run_url(self, url):
        log(f"dispatching {url}")
        job_id = dispatch(self.args.namespace, self.pod, url)
        log(f"  job_id={job_id}")
        return self.show_job(job_id, url=url)

    def show_job(self, job_id, url=None):
        wait_for_job(self.conn, job_id, self.args.timeout)
        url = url or fetch_url(self.conn, job_id)
        rows = fetch_results(self.conn, job_id)
        log(f"  job {job_id}: {len(rows)} library rows")
        rows = [r for r in rows if r["name"] in self.current_libs]
        clusters = {c: cluster_component(rows, c) for c in COMPONENTS}
        self.last_clusters = clusters

        print(f"\n# job_id={job_id}  url={url!r}  "
              f"libraries={len(rows)}/{len(self.all_libs)}")
        print_clusters(clusters, COMPONENTS)

        if len(self.current_libs) == 1:
            (only,) = self.current_libs
            print(f"\n*** narrowed to a single library: {only} ***")
        return clusters


def interactive_loop(session, seed_url=None, seed_job=None):
    # First iteration may be seeded from CLI.
    if seed_job is not None:
        session.show_job(seed_job)
    elif seed_url is not None:
        session.run_url(seed_url)

    while True:
        clusters = session.last_clusters
        if clusters is None:
            prompt = f"\n[{len(session.current_libs)} libs]  URL> "
        else:
            prompt = (f"\n[{len(session.current_libs)} libs]  "
                      "Filter (component:idx... | URL | skip | back | reset | help | quit)> ")
        inp = read_input(prompt).strip()
        if not inp:
            continue
        low = inp.lower()

        if low in ("quit", "q", "exit"):
            return
        if low in ("help", "h", "?"):
            print_help()
            continue
        if low in ("libs", "list", "l"):
            session.list_libs()
            continue
        if low in ("reset", "r"):
            session.reset()
            continue
        if low in ("back", "b", "undo", "u"):
            session.back()
            continue
        if low in ("skip", "s", "next"):
            session.last_clusters = None  # next prompt asks for a URL
            continue
        if low.startswith("job "):
            try:
                jid = int(inp.split(None, 1)[1])
            except (ValueError, IndexError):
                print("usage: job <id>")
                continue
            try:
                session.show_job(jid)
            except Exception as e:
                print(f"  error: {e}")
            continue

        # Try parsing as a cluster filter first (only if we have clusters).
        if clusters is not None:
            try:
                action, payload = parse_filter(inp, clusters)
            except ValueError as e:
                action, payload = None, None
                # Fall through to treat as URL if the input contains "://".
                if "://" not in inp:
                    print(f"  error: {e}")
                    continue
            if action == "set":
                if not payload:
                    print("  no libraries match that filter; ignored")
                    continue
                session.push(payload)
                print(f"kept {len(payload)} libraries: {', '.join(sorted(payload))}")
                # After narrowing, re-render the SAME clusters but restricted.
                # Simpler: just clear clusters so next prompt is for a URL.
                session.last_clusters = None
                continue
            if action == "skip":
                session.last_clusters = None
                continue
            # fall through for unknown — treat as URL below

        # Otherwise treat the line as a URL.
        try:
            session.run_url(inp)
        except Exception as e:
            print(f"  error: {e}")


def main():
    args = parse_args()

    log(f"locating manager pod in {args.namespace}")
    pod = get_manager_pod(args.namespace)
    log(f"  manager pod: {pod}")

    if not args.no_port_forward:
        log(f"starting port-forward svc/postgres -> 127.0.0.1:{args.pg_port}")
        start_port_forward(args.namespace, args.pg_port)

    conn = psycopg2.connect(
        host=args.pg_host, port=args.pg_port, user=args.pg_user,
        password=args.pg_password, dbname=args.pg_db)
    conn.set_session(readonly=True, autocommit=True)

    try:
        session = Session(args, conn, pod)
        log(f"starting with {len(session.current_libs)} libraries; "
            "type 'help' for commands")
        interactive_loop(session, seed_url=args.url, seed_job=args.job_id)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
