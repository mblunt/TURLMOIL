"""Database connection and session management."""

from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session

from .config import config
from .models import Base


engine_kwargs = {
    "echo": False,
    "pool_pre_ping": True,
    "pool_size": 2,
    "max_overflow": 0,
    "pool_timeout": 30,
    "pool_recycle": 1800,
}
if config.database.driver != "sqlite":
    engine_kwargs["connect_args"] = {"options": "-c timezone=utc"}
engine = create_engine(config.database.url, **engine_kwargs)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def dispose_engine(**kwargs):
    """Called after Celery forks a worker process — reset pool so each
    process gets its own connections rather than sharing the parent's."""
    engine.dispose()


try:
    from celery.signals import worker_process_init
    worker_process_init.connect(dispose_engine)
except ImportError:
    pass

def init_db():
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)

@contextmanager
def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def get_session_direct() -> Session:
    return SessionLocal()

def get_db_url() -> str:
    return config.database.url
