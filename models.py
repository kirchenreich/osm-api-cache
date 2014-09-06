from sqlalchemy import (
    BigInteger,
    Binary,
    Column,
    DateTime,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.dialects.postgresql import JSON, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class OsmBase(Base):
    __abstract__ = True

    pk = Column(BigInteger, primary_key=True)
    created_on = Column(TIMESTAMP, default=func.now())
    updated_on = Column(TIMESTAMP, default=func.now(),
                        onupdate=func.now())


class Node(OsmBase):
    __tablename__ = 'node'

    id = Column(BigInteger, unique=True)

    tags = Column(JSON, nullable=True)
    meta = Column(JSON, nullable=True)
    changeset = Column(BigInteger, nullable=True)

    lat = Column(Numeric(9, 6), nullable=True)
    lon = Column(Numeric(9, 6), nullable=True)


class Way(OsmBase):
    __tablename__ = 'way'

    id = Column(BigInteger, unique=True)

    tags = Column(JSON, nullable=True)
    meta = Column(JSON, nullable=True)
    changeset = Column(BigInteger, nullable=True)


class WayMember(OsmBase):
    __tablename__ = 'waymember'

    way_id = Column(BigInteger)
    node_id = Column(BigInteger)

    order = Column(Integer, nullable=True)


class Relation(OsmBase):
    __tablename__ = 'relation'

    id = Column(BigInteger, unique=True)

    tags = Column(JSON, nullable=True)
    meta = Column(JSON, nullable=True)
    changeset = Column(BigInteger, nullable=True)


class RelationMember(OsmBase):
    __tablename__ = 'relationmember'

    relation_id = Column(BigInteger)

    # allowed values: n, w, r
    element_type = Column(String(1))
    element_id = Column(BigInteger)

    order = Column(Integer, nullable=True)
    role = Column(String, nullable=True)
