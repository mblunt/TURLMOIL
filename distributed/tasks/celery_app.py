"""Celery application configuration."""

from celery import Celery

from core.config import config

# Create Celery app
app = Celery("distributed_parser")

# Configure from our config object
app.conf.update(
    broker_url=config.celery.broker_url,
    result_backend=config.celery.result_backend,
    task_serializer=config.celery.task_serializer,
    result_serializer=config.celery.result_serializer,
    accept_content=config.celery.accept_content,
    timezone=config.celery.timezone,
    enable_utc=config.celery.enable_utc,
    task_track_started=config.celery.task_track_started,
    task_time_limit=config.celery.task_time_limit,
    worker_concurrency=config.celery.worker_concurrency,
    
    # Task deduplication and reliability settings
    task_acks_late=True,  # Acknowledge task after completion, not on receipt
    task_reject_on_worker_lost=True,  # Requeue task if worker dies
    worker_prefetch_multiplier=1,  # Take one task at a time to prevent duplication
    
    # Task routing
    task_routes={
        "tasks.differentials.run_differential": {"queue": "differentials"},
        "tasks.differentials.score_and_update":  {"queue": "differentials"},
        "tasks.feedback.reinforce.update_weights": {"queue": "differentials"},
    },

    # Task discovery
    imports=[
        "tasks.parse_url",
        "tasks.generate",
        "tasks.differentials",
        "tasks.feedback.reinforce",
    ],
)


def get_celery_app() -> Celery:
    """Get the Celery application instance."""
    return app
