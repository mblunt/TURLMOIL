"""Tasks module exports."""

from .celery_app import app, get_celery_app
from .parse_url import parse_single, parse_all, parse_url
from .generate import generate_batch
from .differentials import run_differential, score_and_update
from .feedback.reinforce import update_weights

__all__ = [
    # Celery app
    "app",
    "get_celery_app",
    # Parse tasks
    "parse_single",
    "parse_all",
    "parse_url",
    # Generation tasks
    "generate_batch",
    # Differential + feedback tasks
    "run_differential",
    "score_and_update",
    "update_weights",
]

