from sqlalchemy import (
    BigInteger,
    Binary,
    Column,
    DateTime,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import ARRAY, JSON, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Element(Base):
    __tablename__ = 'element'

    id = Column(BigInteger, primary_key=True)
    osm_id = Column(BigInteger, nullable=True, index=True)

    # allowed values: n, w, r
    element_type = Column(String(1))

    changeset = Column(BigInteger, nullable=True)
    attributes = Column(JSON, nullable=True)
    meta = Column(JSON, nullable=True)

    # we need to have the order of members / references to osm_id
    Column("members", ARRAY(Integer))

    created_on = Column(TIMESTAMP, default=func.now())
    updated_on = Column(TIMESTAMP, default=func.now(),
                        onupdate=func.now())
