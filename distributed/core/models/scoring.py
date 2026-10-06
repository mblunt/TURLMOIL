from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from .base import Base

class DifferentialCountMatrix(Base):
    """
    Cross matrix of differential counts between every library pair.
    Each row is a unique (library_a, library_b) pair (a_id <= b_id to avoid duplicates).
    Counts how many times each field disagreed across all jobs seen so far.
    """
    __tablename__ = "library_differential_matrix"

    library_a_id = Column(Integer, ForeignKey("libraries.id", ondelete="CASCADE"), primary_key=True)
    library_b_id = Column(Integer, ForeignKey("libraries.id", ondelete="CASCADE"), primary_key=True)

    scheme     = Column(Integer, default=0)
    authority  = Column(Integer, default=0)
    userinfo   = Column(Integer, default=0)
    username   = Column(Integer, default=0)
    password   = Column(Integer, default=0)
    host       = Column(Integer, default=0)
    port       = Column(Integer, default=0)
    path       = Column(Integer, default=0)
    query      = Column(Integer, default=0)
    query_dict = Column(Integer, default=0)
    fragment   = Column(Integer, default=0)
    total      = Column(Integer, default=0)

    library_a = relationship("Library", foreign_keys=[library_a_id])
    library_b = relationship("Library", foreign_keys=[library_b_id])

    __table_args__ = (
        CheckConstraint("library_a_id <= library_b_id", name="ck_matrix_ordered_pair"),
    )

    def __init__(self, **kwargs):
        # Normalize library pair to ensure (a_id <= b_id) to avoid (A,B) != (B,A) in the matrix
        a = kwargs.pop("library_a_id")
        b = kwargs.pop("library_b_id")
        kwargs["library_a_id"], kwargs["library_b_id"] = min(a, b), max(a, b)
        super().__init__(**kwargs)
