from datetime import datetime, timezone
from sqlalchemy import (
    Column, Integer, String, Text, DateTime, Boolean,
    ForeignKey, JSON, Index, Float, text
)
from sqlalchemy.orm import relationship

from .base import Base
from .enums import JobStatus


class Library(Base):
    """
    A registered URL parser library.

    Represents a URL parsing library/tool with metadata and configuration.
    Used to see which libraries are available for parsing jobs.
    """
    __tablename__ = "libraries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    language = Column(String(64), nullable=False)
    version = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)

    # How to invoke this parser
    binary_path = Column(String(512), nullable=True)  # For compiled parsers
    command = Column(String(512), nullable=True)  # Custom command template

    # Metadata
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    config = Column(JSON, default=dict)

    # Relationships
    results = relationship("ParseResult", back_populates="library", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Library(id={self.id}, name='{self.name}', language={self.language})>"


class ParseJob(Base):
    """
    A URL parsing job (one URL to be parsed by all libraries).

    This is a single URL that needs to be parsed by all registered libraries.
    The results are stored in the ParseResult table, linked by job_id.
    This makes it easier to search for results by URL string, without
    having to deal with the large multiplier of data to sift through in the ParseResult table.

    This is also used to keep track of job status, timestamps, and progress of each library
    in a single place.
    """
    __tablename__ = "parse_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text, nullable=False)
    status = Column(String(32), default=JobStatus.PENDING.value)

    # Tracking
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    # How many libraries have processed this
    libraries_completed = Column(Integer, default=0)
    libraries_total = Column(Integer, default=0)

    # Rarity score (0-100) assigned after differential analysis
    score = Column(Integer, nullable=True)
    scored_at = Column(DateTime, nullable=True)

    # Per-component branch choices recorded at generation time, used by REINFORCE.
    # Format: {"scheme": {"chosen": "p_invalid", "group": "SCHEME"}, ...}
    generation_choices = Column(JSON, nullable=True)

    # Relationships
    results = relationship("ParseResult", back_populates="job", cascade="all, delete-orphan")

    __table_args__ = (
        Index("idx_parse_jobs_status", "status"),
        Index("idx_parse_jobs_url", "url"),
        Index("idx_parse_jobs_score_id", "id", postgresql_where=text("score IS NOT NULL")),
    )


class ParseResult(Base):
    """
    Result of parsing a URL with a specific library.

    This is the detailed result of parsing a single URL (from ParseJob)
    using a specific library (from Library). It contains the parsed components,
    success status, error messages, timing information, and raw output for debugging.
    """
    __tablename__ = "parse_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey("parse_jobs.id", ondelete="CASCADE"), nullable=False)
    library_id = Column(Integer, ForeignKey("libraries.id", ondelete="CASCADE"), nullable=False)

    # Result data
    success = Column(Boolean, nullable=False)
    error_message = Column(Text, nullable=True)
    parse_time_ms = Column(Float, nullable=True)

    # Parsed URL components (nullable for failed parses)
    scheme = Column(Text, nullable=True)
    authority = Column(Text, nullable=True)
    userinfo = Column(Text, nullable=True)
    username = Column(Text, nullable=True)
    password = Column(Text, nullable=True)
    host = Column(Text, nullable=True)
    port = Column(Text, nullable=True)
    path = Column(Text, nullable=True)
    query = Column(Text, nullable=True)
    query_dict = Column(JSON, nullable=True)  # This needs to be packaged appropriately per library to JSON.
    fragment = Column(Text, nullable=True)

    # Raw output for seeing what the library said about the URL
    # This is important for diagnosing parsing discrepancies
    raw_output = Column(JSON, nullable=True)

    # Timing
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    job = relationship("ParseJob", back_populates="results")
    library = relationship("Library", back_populates="results")

    __table_args__ = (
        Index("idx_parse_results_job", "job_id"),
        Index("idx_parse_results_library", "library_id"),
        Index("idx_parse_results_job_library", "job_id", "library_id", unique=True),
    )
