from datetime import datetime, timezone
from sqlalchemy import (
    Column, Integer, String, DateTime, Index,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .base import Base

class Differential(Base):
    """
    Represents a differential between two parse results for the same URL.

    One row per (job, library_a, library_b, component) triple that differed.
    library_a_id/library_b_id are denormalized (always a_id <= b_id) to make
    pair-frequency queries fast without joining through parse_results.
    """
    __tablename__ = "differentials"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey("parse_jobs.id", ondelete="CASCADE"), nullable=False)
    parse_result_a_id = Column(Integer, ForeignKey("parse_results.id", ondelete="CASCADE"), nullable=False)
    parse_result_b_id = Column(Integer, ForeignKey("parse_results.id", ondelete="CASCADE"), nullable=False)

    # Denormalized for fast pair-frequency queries (no join needed)
    library_a_id = Column(Integer, ForeignKey("libraries.id", ondelete="CASCADE"), nullable=False)
    library_b_id = Column(Integer, ForeignKey("libraries.id", ondelete="CASCADE"), nullable=False)

    differential_type = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    job = relationship("ParseJob")
    parse_result_a = relationship("ParseResult", foreign_keys=[parse_result_a_id])
    parse_result_b = relationship("ParseResult", foreign_keys=[parse_result_b_id])

    __table_args__ = (
        Index("idx_differentials_job_id", "job_id"),
        Index("idx_differentials_pair_type", "library_a_id", "library_b_id", "differential_type"),
        Index("idx_differentials_type", "differential_type"),
    )
