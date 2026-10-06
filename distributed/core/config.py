"""Central configuration for the distributed system."""

import os
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import quote_plus


@dataclass
class RedisConfig:
    host: str = os.getenv("REDIS_HOST", "redis")
    port: int = int(os.getenv("REDIS_PORT", "6379"))
    db: int = int(os.getenv("REDIS_DB", "0"))
    password: Optional[str] = os.getenv("REDIS_PASSWORD")
    
    @property
    def url(self) -> str:
        auth = f":{self.password}@" if self.password else ""
        return f"redis://{auth}{self.host}:{self.port}/{self.db}"


@dataclass
class DatabaseConfig:
    """Database connection configuration."""
    driver: str = os.getenv("DB_DRIVER", "sqlite")
    host: str = os.getenv("DB_HOST", "localhost")
    port: int = int(os.getenv("DB_PORT", "5432"))
    name: str = os.getenv("DB_NAME", "url_parser.db")
    user: str = os.getenv("DB_USER", "")
    password: str = os.getenv("DB_PASSWORD", "")
    
    @property
    def url(self) -> str:
        if self.driver == "sqlite":
            return f"sqlite:///{self.name}"
        return f"postgresql://{quote_plus(self.user)}:{quote_plus(self.password)}@{self.host}:{self.port}/{self.name}"


@dataclass
class CeleryConfig:
    """Celery configuration."""
    broker_url: str = field(default_factory=lambda: RedisConfig().url)
    result_backend: str = field(default_factory=lambda: RedisConfig().url)
    task_serializer: str = "json"
    result_serializer: str = "json"
    accept_content: list = field(default_factory=lambda: ["json"])
    timezone: str = "UTC"
    enable_utc: bool = True
    task_track_started: bool = True
    task_time_limit: int = 300 # seconds
    worker_concurrency: int = int(os.getenv("CELERY_CONCURRENCY", "4"))


@dataclass 
class Config:
    """Main configuration container."""
    redis: RedisConfig = field(default_factory=RedisConfig)
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    celery: CeleryConfig = field(default_factory=CeleryConfig)
    
    # Fuzzing settings
    batch_size: int = int(os.getenv("BATCH_SIZE", "1"))
    buffer_size: int = int(os.getenv("BUFFER_SIZE", "10000"))
    
    # Parser settings
    parse_timeout: float = float(os.getenv("PARSE_TIMEOUT", "5.0"))


# Global config instance
config = Config()
