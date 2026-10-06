#!/usr/bin/env python3
"""Manager service entry point."""

import sys
import argparse
import logging
import signal
import json
import time
from typing import Optional, List

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("manager")


def init_database():
    from core.database import init_db
    init_db()


def get_enabled_libraries():
    from core.database import get_session
    from core.models import Library
    with get_session() as session:
        return [lib.id for lib in session.query(Library).filter_by(enabled=True).all()]


def get_queue_depths(languages):
    import redis as redis_lib
    from core.config import config
    r = redis_lib.Redis(host=config.redis.host, port=config.redis.port, decode_responses=True)
    return {lang: r.llen(lang) for lang in languages}


def run_fuzzing_loop(batch_size: int = 1, max_pending: int = 1000, delay: float = 0.0):
    from tasks import generate_batch
    from core.database import get_session
    from core.models import Library

    if not get_enabled_libraries():
        logger.error("No enabled libraries found.")
        return

    with get_session() as session:
        languages = list({lib.language for lib in session.query(Library).filter_by(enabled=True).all()})

    logger.info(f"Starting fuzzing (batch_size={batch_size}, max_pending={max_pending}/language, delay={delay}s)")

    while True:
        try:
            depths = get_queue_depths(languages)
            overloaded = {lang: depth for lang, depth in depths.items() if depth >= max_pending}

            if overloaded:
                worst = max(overloaded, key=overloaded.get)
                logger.info(f"Backpressure: {len(overloaded)} queues over {max_pending} (worst: {worst}={overloaded[worst]}), waiting...")
                time.sleep(5)
                continue

            result = generate_batch.delay(n=batch_size).get(timeout=120)
            count = result.get("count", 0)
            active = {l: d for l, d in depths.items() if d > 0}
            logger.info(f"Created {count} jobs | queues: {active}")

            if delay > 0:
                time.sleep(delay)
        except Exception as e:
            logger.error(f"Batch failed: {e}")


def run_analysis_loop(max_pending: int = 500, delay: float = 1.0):
    """Dispatch differential analysis for completed jobs, respecting a concurrency cap.

    Checks how many jobs are currently in PROCESSING state and only dispatches
    more when below max_pending, matching the same backpressure pattern as the
    fuzzing loop.
    """
    import redis as redis_lib
    from tasks.differentials import run_differential
    from core.database import get_session
    from core.models import ParseJob, JobStatus
    from core.config import config

    r = redis_lib.Redis(host=config.redis.host, port=config.redis.port, decode_responses=True)

    MAX_PROCESSING = max_pending * 2

    logger.info(f"Starting differential analysis loop (max_pending={max_pending}, max_processing={MAX_PROCESSING})")
    while True:
        try:
            pending = r.llen("differentials")

            if pending >= max_pending:
                logger.info(f"Backpressure: {pending} tasks queued, waiting...")
                time.sleep(5)
                continue

            with get_session() as session:
                processing = session.query(ParseJob).filter(
                    ParseJob.status == JobStatus.PROCESSING.value
                ).count()

            if processing >= MAX_PROCESSING:
                logger.info(f"Backpressure: {processing} jobs in PROCESSING state, waiting...")
                time.sleep(5)
                continue

            slots = min(max_pending - pending, MAX_PROCESSING - processing)
            with get_session() as session:
                job_ids = [jid for (jid,) in session.query(ParseJob.id).filter(
                    ParseJob.status == JobStatus.COMPLETED.value
                ).limit(slots).all()]

            if not job_ids:
                logger.info("No completed jobs pending differential analysis, waiting...")
                time.sleep(10)
                continue

            for job_id in job_ids:
                run_differential.delay(job_id)
            logger.info(f"Dispatched {len(job_ids)} differential tasks | queue depth: {pending}")

            if delay > 0:
                time.sleep(delay)
        except Exception as e:
            logger.error(f"Analysis dispatch failed: {e}")
            time.sleep(5)


def register_library(name: str, language: str, version: str, binary_path: Optional[str] = None):
    from core.database import get_session
    from core.models import Library

    # Normalise aliases
    lang = {"js": "javascript", "c++": "cpp", "c#": "csharp"}.get(language.lower(), language.lower())

    with get_session() as session:
        if session.query(Library).filter_by(name=name).first():
            logger.error(f"Library already exists: {name}")
            return
        session.add(Library(
            name=name,
            language=lang,
            version=version,
            binary_path=binary_path,
            enabled=True,
        ))
        session.commit()
        logger.info(f"Registered: {name}")


def list_libraries():
    from core.database import get_session
    from core.models import Library

    with get_session() as session:
        libraries = session.query(Library).all()
        if not libraries:
            print("No libraries registered")
            return
        print(f"\n{'ID':<4} {'Name':<20} {'Language':<12} {'Version':<10} {'Enabled':<8} Path")
        print("-" * 80)
        for lib in libraries:
            path = lib.binary_path or "N/A"
            if len(path) > 30:
                path = "..." + path[-27:]
            lang = lib.language
            print(f"{lib.id:<4} {lib.name:<20} {lang:<12} {lib.version or 'N/A':<10} {'Yes' if lib.enabled else 'No':<8} {path}")


def show_stats():
    from core.database import get_session
    from core.models import ParseJob, ParseResult, Library, JobStatus

    with get_session() as session:
        total_jobs = session.query(ParseJob).count()
        by_status = {s.value: session.query(ParseJob).filter(ParseJob.status == s).count() for s in JobStatus}
        total_results = session.query(ParseResult).count()
        total = session.query(Library).count()
        enabled = session.query(Library).filter(Library.enabled == True).count()

    print(f"\nJobs: {total_jobs}")
    for status, count in by_status.items():
        print(f"  {status:<15} {count}")
    print(f"Results: {total_results}")
    print(f"Libraries: {enabled}/{total} enabled")


def test_url(url: str, field: Optional[str] = None):
    from core.database import get_session
    from core.models import Library, ParseResult, ParseJob
    from tasks.parse_url import parse_url as parse_url_task
    from time import sleep, time as now

    def _print_table(headers: List[str], rows: List[List[str]]):
        widths = [max(len(h), max((len(str(r[i])) for r in rows), default=0)) for i, h in enumerate(headers)]
        print(" | ".join(h.ljust(widths[i]) for i, h in enumerate(headers)))
        print("-+-".join('-' * w for w in widths))
        for r in rows:
            print(" | ".join(str(r[i]).ljust(widths[i]) for i in range(len(headers))))

    print(f"\nDispatching URL to workers: {url}\n")
    try:
        res = parse_url_task.delay(url).get(timeout=10)
        job_id = res.get("job_id")
    except Exception:
        print("Failed to create remote parse job.")
        return

    if not job_id:
        print(f"Failed to create job for URL: {url}")
        return

    with get_session() as session:
        lib_count = session.query(Library).filter(Library.enabled == True).count()

    print(f"Job created: {job_id}. Waiting for {lib_count} results (timeout 30s)...")
    start = now()
    while now() - start < 30:
        with get_session() as session:
            result_count = session.query(ParseResult).filter(
                ParseResult.job_id == job_id
            ).count()
            if result_count >= lib_count:
                break
        sleep(0.2)
    else:
        print("Timeout; fetching available results.")

    with get_session() as session:
        libs = session.query(Library).filter(Library.enabled == True).order_by(Library.name).all()
        if not libs:
            print("No enabled libraries registered.")
            return
        lib_ids = [lib.id for lib in libs]
        prs_map = {pr.library_id: pr for pr in session.query(ParseResult).filter(
            ParseResult.job_id == job_id, ParseResult.library_id.in_(lib_ids)
        ).all()}

        if field:
            rows = []
            for lib in libs:
                pr = prs_map.get(lib.id)
                if not pr:
                    val = "MISSING"
                elif not pr.success:
                    val = f"ERROR: {pr.error_message or 'failed'}"
                else:
                    val = getattr(pr, field, None)
                    if val is None:
                        val = (pr.raw_output or {}).get(field, '-')
                    if isinstance(val, (dict, list)):
                        val = json.dumps(val, ensure_ascii=False)
                rows.append([lib.name, str(val)])
            _print_table(["Library", field], rows)
            return

        headers = ["Library", "OK", "ms", "scheme", "authority", "userinfo",
                   "username", "password", "host", "port", "path", "query", "query_dict", "fragment"]
        rows = []
        for lib in libs:
            pr = prs_map.get(lib.id)
            if not pr:
                rows.append([lib.name, "MISSING"] + ["-"] * (len(headers) - 2))
                continue
            ms = f"{pr.parse_time_ms:.2f}" if pr.parse_time_ms else "-"
            if not pr.success:
                rows.append([lib.name, "N", ms, f"ERROR: {pr.error_message or 'failed'}"] + ["-"] * (len(headers) - 4))
            else:
                qd = '-'
                if pr.query_dict:
                    qd = json.dumps(pr.query_dict, ensure_ascii=False)
                    if len(qd) > 50:
                        qd = qd[:47] + "..."
                rows.append([lib.name, "Y", ms,
                    pr.scheme or '-', pr.authority or '-', pr.userinfo or '-',
                    pr.username or '-', pr.password or '-', pr.host or '-',
                    pr.port or '-', pr.path or '-', pr.query or '-', qd, pr.fragment or '-'])
        _print_table(headers, rows)


def main():
    parser = argparse.ArgumentParser(description="Parser testing manager")
    sub = parser.add_subparsers(dest="command")

    fuzz = sub.add_parser("fuzz")
    fuzz.add_argument("--batch-size", "-b", type=int, default=1)
    fuzz.add_argument("--max-pending", "-m", type=int, default=1000)
    fuzz.add_argument("--delay", "-d", type=float, default=0.0)

    analyze = sub.add_parser("analyze")
    analyze.add_argument("--max-pending", "-m", type=int, default=500)
    analyze.add_argument("--delay", "-d", type=float, default=1.0)

    sub.add_parser("stats")
    sub.add_parser("list")
    sub.add_parser("init")

    reg = sub.add_parser("register")
    reg.add_argument("name")
    reg.add_argument("language")
    reg.add_argument("version")
    reg.add_argument("--binary")

    for cmd in ("enable", "disable", "delete"):
        p = sub.add_parser(cmd)
        p.add_argument("name")
        if cmd == "delete":
            p.add_argument("--force", "-f", action="store_true")

    test = sub.add_parser("test")
    test.add_argument("url")
    test.add_argument("field", nargs='?')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

    if args.command == "analyze":
        init_database()
        run_analysis_loop(args.max_pending, args.delay)
    elif args.command == "init":
        init_database()
    elif args.command == "fuzz":
        init_database()
        # threading.Thread(target=run_analysis_loop, daemon=True).start()  # differential analysis disabled
        run_fuzzing_loop(args.batch_size, args.max_pending, args.delay)
    elif args.command == "stats":
        init_database()
        show_stats()
    elif args.command == "register":
        init_database()
        register_library(args.name, args.language, args.version, args.binary)
    elif args.command == "list":
        init_database()
        list_libraries()
    elif args.command in ("enable", "disable", "delete"):
        init_database()
        from registry.library import LibraryRegistry
        if args.command == "delete":
            if not args.force and input(f"Delete '{args.name}'? [y/N] ").strip().lower() != "y":
                print("Aborted.")
                return
            if LibraryRegistry.delete(args.name):
                logger.info(f"Deleted: {args.name}")
            else:
                logger.error(f"Not found: {args.name}")
        else:
            getattr(LibraryRegistry, args.command)(args.name)
            logger.info(f"{args.command.capitalize()}d: {args.name}")
    elif args.command == "test":
        init_database()
        test_url(args.url, getattr(args, 'field', None))


if __name__ == "__main__":
    main()