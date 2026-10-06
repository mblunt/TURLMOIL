#!/usr/bin/env python3
"""
build_scheme_matrix.py

Compute, for every pair of enabled URL parsers, the fraction of *eligible*
URL components that exhibit at least one differential. Output is a flat CSV
suitable for rendering a heatmap.

Definitions
-----------
Components (11):
    scheme, authority, userinfo, username, password, host, port,
    path, query, query_dict, fragment

A component is EXCLUDED for a library if that library ever emits the marker
"EXCLUDE" for it (the library exposes no method to extract that field).

For a pair (A, B):
    excluded_fields = components excluded by A OR by B
    eligible_fields = 11 - excluded_fields
    differential_count = number of eligible components on which A and B
                          disagree at least once
    ratio = differential_count / eligible_fields * 100   (0 when eligible = 0)

Optimization notes
------------------
- The differential set is obtained with ONE DISTINCT scan over
  idx_diff_pair_type (library_a_id, library_b_id, differential_type).
  DISTINCT short-circuits per (pair, component) at the storage layer, which
  is the same "stop after the first hit" semantics as a per-component
  LIMIT 1, without ~50k client/server round trips.
- Pairs are normalized with LEAST/GREATEST and the scan is ORDER BY lo, hi
  so the result streams pair-by-pair through a named (server-side) cursor.
- The eleven EXCLUDE column scans are folded into a single aggregate pass
  using bool_or().
"""

import argparse
import csv
import os
import sys
import time
from itertools import combinations

import psycopg2
import psycopg2.extras

COMPONENTS = (
    "scheme", "authority", "userinfo", "username", "password",
    "host", "port", "path", "query", "query_dict", "fragment",
)
TOTAL_COMPONENTS = len(COMPONENTS)  # 11
EXCLUDE_MARKER = "EXCLUDE"


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", file=sys.stderr, flush=True)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pg-host", default=os.environ.get("PGHOST", "localhost"))
    p.add_argument("--pg-port", default=int(os.environ.get("PGPORT", "5432")), type=int)
    p.add_argument("--pg-user", default=os.environ.get("PGUSER", "parser"))
    p.add_argument("--pg-password", default=os.environ.get("PGPASSWORD", "PLACEHOLDER_CHANGE_BEFORE_REPRO"))
    p.add_argument("--pg-db", default=os.environ.get("PGDATABASE", "url_parser"))
    p.add_argument("--out", default="scheme_matrix.csv",
                   help="output CSV path")
    p.add_argument("--flush-every", type=int, default=200,
                   help="flush the output file every N matrix rows")
    p.add_argument("--itersize", type=int, default=20000,
                   help="server-side cursor fetch size for the differential scan")
    p.add_argument("--include-exclude-type", action="store_true",
                   help="treat differential_type = 'EXCLUDE' as a real component "
                        "(default: dropped, matching the methodology)")
    return p.parse_args()


def fetch_enabled_libraries(conn):
    """Return list of (id, name) for enabled libraries, ordered by name."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, name FROM libraries WHERE enabled = TRUE ORDER BY name"
        )
        rows = cur.fetchall()
    return rows


def fetch_exclude_map(conn):
    """
    One aggregate pass over parse_results. Returns {library_id: frozenset(excluded_components)}.

    A library "excludes" a component if it ever emits the EXCLUDE marker for it.
    query_dict is stored as json/text, so it is normalized before comparison.
    """
    # Build "bool_or(col = 'EXCLUDE') AS col" for each component. query_dict special-cased.
    select_parts = []
    for c in COMPONENTS:
        if c == "query_dict":
            select_parts.append(
                "bool_or(TRIM('\"' FROM COALESCE(query_dict::text, '')) = %(m)s) AS query_dict"
            )
        else:
            select_parts.append(f"bool_or({c} = %(m)s) AS {c}")
    sql = (
        "SELECT library_id, " + ", ".join(select_parts) +
        " FROM parse_results GROUP BY library_id"
    )

    excl = {}
    with conn.cursor() as cur:
        cur.execute(sql, {"m": EXCLUDE_MARKER})
        colnames = [d[0] for d in cur.description]
        comp_idx = {name: i for i, name in enumerate(colnames)}
        for row in cur:
            lib_id = row[comp_idx["library_id"]]
            excluded = frozenset(
                c for c in COMPONENTS if row[comp_idx[c]]
            )
            excl[lib_id] = excluded
    return excl


def stream_pair_differentials(conn, enabled_ids, itersize, include_exclude_type):
    """
    Single DISTINCT index scan, streamed pair-by-pair (ORDER BY lo, hi).

    Returns {(lo, hi): frozenset(components_with_at_least_one_differential)}.
    Pairs are normalized so lo < hi. Only enabled libraries are kept.
    """
    type_filter = "" if include_exclude_type else \
        f" AND differential_type <> '{EXCLUDE_MARKER}'"

    sql = f"""
        SELECT
            LEAST(library_a_id, library_b_id)    AS lo,
            GREATEST(library_a_id, library_b_id) AS hi,
            differential_type
        FROM differentials
        WHERE TRUE{type_filter}
        GROUP BY 1, 2, 3
        ORDER BY 1, 2
    """

    enabled = set(enabled_ids)
    pair_diffs = {}
    rows_seen = 0
    pairs_done = 0

    # Named cursor => server-side, streamed in chunks of itersize.
    with conn.cursor(name="diff_stream") as cur:
        cur.itersize = itersize
        cur.execute(sql)

        cur_pair = None
        cur_set = set()

        def flush_pair(pair, comps):
            nonlocal pairs_done
            if pair is None:
                return
            lo, hi = pair
            if lo in enabled and hi in enabled and comps:
                pair_diffs[pair] = frozenset(comps)
            pairs_done += 1

        for lo, hi, dtype in cur:
            rows_seen += 1
            pair = (lo, hi)
            if pair != cur_pair:
                flush_pair(cur_pair, cur_set)
                cur_pair = pair
                cur_set = set()
                if pairs_done and pairs_done % 500 == 0:
                    log(f"  scan: {pairs_done} pairs, {rows_seen} rows")
            cur_set.add(dtype)

        flush_pair(cur_pair, cur_set)

    log(f"  scan complete: {rows_seen} rows over {pairs_done} differing pairs")
    return pair_diffs


def write_matrix(libraries, excl_map, pair_diffs, out_path, flush_every):
    """
    Emit one row per ordered (a, b) pair, including the diagonal, ordered by
    library name. Flush periodically so a crash leaves partial results on disk.
    """
    # Libraries that never appeared in parse_results have no exclude record.
    # Treat them as excluding nothing.
    empty = frozenset()

    tmp_path = out_path + ".partial"
    written = 0
    total = len(libraries) * len(libraries)
    t0 = time.time()

    try:
        from tqdm import tqdm
        bar = tqdm(total=total, unit="cell", desc="matrix")
    except Exception:
        bar = None

    with open(tmp_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "library_a", "library_b",
            "differential_count", "eligible_fields", "excluded_fields", "ratio",
        ])

        for a_id, a_name in libraries:
            a_excl = excl_map.get(a_id, empty)
            for b_id, b_name in libraries:
                if a_id == b_id:
                    # Diagonal: deterministic parser, no self-differential.
                    w.writerow([a_name, b_name, 0, TOTAL_COMPONENTS, 0, "0.00"])
                else:
                    b_excl = excl_map.get(b_id, empty)
                    excluded = a_excl | b_excl
                    excluded_fields = len(excluded)
                    eligible = set(COMPONENTS) - excluded
                    eligible_fields = len(eligible)

                    lo, hi = (a_id, b_id) if a_id < b_id else (b_id, a_id)
                    diff_set = pair_diffs.get((lo, hi), empty) & eligible
                    differential_count = len(diff_set)

                    if differential_count > 0 and eligible_fields > 0:
                        ratio = differential_count / eligible_fields * 100.0
                    else:
                        ratio = 0.0

                    w.writerow([
                        a_name, b_name,
                        differential_count, eligible_fields, excluded_fields,
                        f"{ratio:.2f}",
                    ])

                written += 1
                if bar is not None:
                    bar.update(1)
                if written % flush_every == 0:
                    f.flush()
                    os.fsync(f.fileno())

    if bar is not None:
        bar.close()

    os.replace(tmp_path, out_path)
    log(f"  wrote {written} cells in {time.time() - t0:.1f}s -> {out_path}")


def main():
    args = parse_args()

    log(f"connecting to {args.pg_user}@{args.pg_host}:{args.pg_port}/{args.pg_db}")
    conn = psycopg2.connect(
        host=args.pg_host, port=args.pg_port, user=args.pg_user,
        password=args.pg_password, dbname=args.pg_db,
    )
    conn.set_session(readonly=True, autocommit=True)

    try:
        log("loading enabled libraries")
        libraries = fetch_enabled_libraries(conn)
        log(f"  {len(libraries)} enabled libraries "
            f"({len(libraries) * (len(libraries) - 1) // 2} unique pairs)")

        log("computing EXCLUDE map (single aggregate pass over parse_results)")
        t0 = time.time()
        excl_map = fetch_exclude_map(conn)
        log(f"  done in {time.time() - t0:.1f}s")

        log("scanning differentials (single DISTINCT index scan, streamed)")
        t0 = time.time()
        enabled_ids = [lib_id for lib_id, _ in libraries]
        pair_diffs = stream_pair_differentials(
            conn, enabled_ids, args.itersize, args.include_exclude_type
        )
        log(f"  done in {time.time() - t0:.1f}s")

        log("building matrix")
        write_matrix(libraries, excl_map, pair_diffs, args.out, args.flush_every)

        log("complete")
    finally:
        conn.close()


if __name__ == "__main__":
    main()