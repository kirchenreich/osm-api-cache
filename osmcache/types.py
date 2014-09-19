
import models

class Node(object):

    __slots__ = ('id', 'lat', 'lon', 'version', 'timestamp', 'changeset',
                 'tags')

    def __init__(self, id, lat, lon, version, timestamp, changeset, **kwargs):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.version = version
        self.timestamp = timestamp
        self.changeset = changeset
        self.tags = {}

    def __getstate__(self):
        return (self.id, self.lat, self.lon, self.version, self.timestamp,
                self.changeset, self.tags)

    def __setstate__(self, state):
        self.id, self.lat, self.lon, self.version, self.timestamp, \
        self.changeset, self.tags = state

    def to_sqlalchemy_model(self):
        return models.Node(
            id=self.id,
            tags=self.tags,
            meta={
                'version': self.version,
                'timestamp': self.timestamp,
            },
            changeset=self.changeset,
            lat=self.lat,
            lon=self.lon
        )

class Way(object):

    __slots__ = ('id', 'version', 'timestamp', 'changeset', 'tags', 'nodes')

    def __init__(self, id, version, timestamp, changeset, **kwargs):
        self.id = id
        self.version = version
        self.timestamp = timestamp
        self.changeset = changeset
        self.tags = {}
        self.nodes = []

    def __getstate__(self):
        return (self.id, self.version, self.timestamp, self.changeset,
                self.tags, self.nodes)

    def __setstate__(self, state):
        self.id, self.version, self.timestamp, self.changeset, \
        self.tags, self.nodes = state

class Relation(object):

    __slots__ = ('id', 'version', 'timestamp', 'changeset', 'tags', 'members')

    def __init__(self, id, version, timestamp, changeset, **kwargs):
        self.id = id
        self.version = version
        self.timestamp = timestamp
        self.changeset = changeset

        self.tags = {}
        self.members = []

    def __getstate__(self):
        return (self.id, self.version, self.timestamp, self.changeset,
                self.tags, self.members)

    def __setstate__(self, state):
        self.id, self.version, self.timestamp, self.changeset, \
        self.tags, self.members = state

