from sqlalchemy import Column, Integer, JSON, CheckConstraint
from .base import Base


class ParserWeights(Base):
    """
    Current weights for each URL component in the scoring algorithm.

    Singleton table (always id=1). Use ParserWeights.get(session) to fetch,
    and ParserWeights.upsert(session, weights) to update.
    """
    __tablename__ = "parser_weights"
    __table_args__ = (
        CheckConstraint("id = 1", name="ck_parser_weights_singleton"),
    )

    id = Column(Integer, primary_key=True, default=1)

    @classmethod
    def get(cls, session):
        return session.get(cls, 1)

    @classmethod
    def upsert(cls, session, **weights):
        row = session.get(cls, 1)
        if row is None:
            row = cls(id=1, **weights)
            session.add(row)
        else:
            for key, value in weights.items():
                setattr(row, key, value)
        return row
    scheme = Column(JSON, nullable=False)
    schemeauthdelim = Column(JSON, nullable=False)
    username = Column(JSON, nullable=False)
    userpassdelim = Column(JSON, nullable=False)
    password = Column(JSON, nullable=False)
    userinfohostdelim = Column(JSON, nullable=False)
    host = Column(JSON, nullable=False)
    hostportdelim = Column(JSON, nullable=False)
    port = Column(JSON, nullable=False)
    authpathdelim = Column(JSON, nullable=False)
    path = Column(JSON, nullable=False)
    pathquerydelim = Column(JSON, nullable=False)
    query = Column(JSON, nullable=False)
    queryfragdelim = Column(JSON, nullable=False)
    fragment = Column(JSON, nullable=False)
    transformation = Column(JSON, nullable=True)
