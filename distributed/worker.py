#!/usr/bin/env python3
"""Celery worker entry point."""

import os
import sys
import argparse
import logging
import time
import socket
import json
from sqlalchemy import update

from core.models import Library
from core.database import init_db, get_session
from core.config import config


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("worker")

WORKER_PARSERS_CONFIG = "/parsers/worker_parsers.json"


def load_parsers_config():
    with open(WORKER_PARSERS_CONFIG, 'r') as f:
        return json.load(f)


def register_parser(session, name, language, version, binary_path, description=""):
    existing = session.query(Library).filter_by(name=name).first()
    if existing:
        session.execute(update(Library).where(Library.name == name).values(
            binary_path=binary_path, language=language,
            version=version, description=description, enabled=True,
        ))
        logger.debug(f"  updated:     {name} ({binary_path})")
    else:
        session.add(Library(
            name=name, language=language, version=version,
            binary_path=binary_path, description=description, enabled=True,
        ))
        logger.debug(f"  registered:  {name} ({binary_path})")
    session.commit()


def wait_for_dns(hostname, max_retries=10, retry_delay=1):
    for attempt in range(max_retries):
        try:
            socket.gethostbyname(hostname)
            logger.debug(f"DNS resolved '{hostname}'")
            return True
        except socket.gaierror:
            if attempt < max_retries - 1:
                logger.warning(f"DNS '{hostname}' not ready, retry {attempt+1}/{max_retries} in {retry_delay}s")
                time.sleep(retry_delay)
                retry_delay = min(retry_delay * 2, 5)
            else:
                return False


def init_parsers():
    parsers_list = load_parsers_config()['parsers']
    logger.info(f"Registering {len(parsers_list)} parsers from {WORKER_PARSERS_CONFIG}")

    with get_session() as session:
        for p in parsers_list:
            register_parser(
                session,
                name=p['id'],
                language=p['language'].lower(),
                version=p['version'],
                binary_path=p['command'],
                description=f"{p['library']} ({p['language']})",
            )

    logger.info(f"Parser registration complete ({len(parsers_list)} parsers)")


def _detect_language() -> str:
    """Infer this worker's language from its parser config, with env var override."""
    override = os.environ.get("WORKER_LANGUAGE", "").strip().lower()
    if override:
        return override
    try:
        with open(WORKER_PARSERS_CONFIG, "r") as f:
            parsers = json.load(f).get("parsers", [])
        languages = {p["language"].lower() for p in parsers if p.get("language")}
        if len(languages) == 1:
            return languages.pop()
        if languages:
            logger.warning(f"Multiple languages in {WORKER_PARSERS_CONFIG}: {languages} — using celery only")
    except Exception as e:
        logger.warning(f"Could not detect language from {WORKER_PARSERS_CONFIG}: {e}")
    return ""


def wait_for_db():
    db_host = config.database.host
    logger.info(f"Resolving database host '{db_host}'...")
    if not wait_for_dns(db_host):
        logger.error(f"DNS resolution failed for '{db_host}' — cannot reach database")
        sys.exit(1)

    logger.info("Connecting to database...")
    max_retries = 30
    retry_delay = 2
    for attempt in range(1, max_retries + 1):
        try:
            init_db()
            logger.info("Database schema ready")
            return
        except Exception as e:
            if attempt < max_retries:
                logger.warning(f"DB not ready (attempt {attempt}/{max_retries}): {e}")
                time.sleep(retry_delay)
            else:
                logger.error(f"Database unreachable after {max_retries} attempts — giving up")
                raise


def main():
    parser = argparse.ArgumentParser(description="Parser testing worker")
    parser.add_argument("--concurrency", "-c", type=int,
        default=int(os.environ.get("CELERY_CONCURRENCY", 4)))
    parser.add_argument("--loglevel", "-l", type=str, default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    parser.add_argument("--hostname", "-n", type=str, default=None)
    args = parser.parse_args()

    language = _detect_language()
    queues = f"celery,{language}" if language else "celery"

    logger.info("=== Parser worker starting ===")
    logger.info(f"  concurrency={args.concurrency}  queues={queues}  loglevel={args.loglevel}")

    wait_for_db()

    from tasks import app
    from celery.signals import worker_ready, worker_shutdown

    @worker_ready.connect
    def on_worker_ready(**kwargs):
        logger.info("Worker ready — registering parsers with database")
        try:
            init_parsers()
            logger.info("Worker fully initialized and accepting tasks")
        except Exception as e:
            logger.error(f"Parser registration failed: {e}", exc_info=True)

    @worker_shutdown.connect
    def on_worker_shutdown(**kwargs):
        logger.info("Worker shutting down")

    worker_args = [
        "worker",
        f"--concurrency={args.concurrency}",
        f"--queues={queues}",
        f"--loglevel={args.loglevel}",
    ]
    if args.hostname:
        worker_args.append(f"--hostname={args.hostname}")

    logger.info(f"Handing off to Celery: {' '.join(worker_args)}")
    app.worker_main(argv=worker_args)


if __name__ == "__main__":
    main()
