#import pytest
from models import Node
from osmcache import session


def test_create_node():
    # <node id="3" lat="50.1240327" lon="14.4524155" timestamp="2012-07-24T12:48:39Z" version="7" changeset="12465837" user="OSMF Redaction Account" uid="722137"/>
    n = Node(id=3, lat=50.1240327, lon=14.4524155,
             changeset=12465837,
             meta={"timestamp":"2012-07-24T12:48:39Z", "version":"7"})
    session.add(n)
    session.commit()
    nx = session.query(Node).filter_by(id=3).first()
    assert nx.id == 3
    assert len(nx.meta.keys()) == 2
    session.delete(nx)
    session.commit()


def test_create_way():
    # should call helper function that creates way in database on base of testdataset
    pass