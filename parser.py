from lxml import etree


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

class Way(object):

    __slots__ = ('id', 'version', 'timestamp', 'changeset', 'tags', 'nodes')

    def __init__(self, id, version, timestamp, changeset, **kwargs):
        self.id = id
        self.version = version
        self.timestamp = timestamp
        self.changeset = changeset
        self.tags = {}
        self.nodes = []

class Relation(object):

    def __init__(self, id, version, timestamp, changeset, **kwargs):
        self.id = id
        self.version = version
        self.timestamp = timestamp
        self.changeset = changeset

        self.tags = {}
        self.members = []

class OSMParser(object):

    def __init__(self, osm_file):
        self.osm_file = osm_file

    def iterparser(self):
        iterparser = etree.iterparse(self.osm_file, events=("start", "end",))

        item = None
        for action, element in iterparser:
            if action == "start":
                if item is None:
                    if element.tag == "node":
                        item = Node(**element.attrib)
                    elif element.tag == "way":
                        item = Way(**element.attrib)
                    elif element.tag == "relation":
                        item = Relation(**element.attrib)
                else:
                    if element.tag == "nd":
                        item.nodes.append(element.get("ref"))
                    elif element.tag == "tag":
                        item.tags[element.get("k")] = element.get("v")
                    elif element.tag == "member":
                        item.members.append((
                            element.get("type"), element.get("ref"),
                            element.get("role")
                        ))
                    else:
                        print("Tag %s under item %s" % (element.tag, item))
            else:
                if element.tag in ("node", "way", "relation"):
                    yield item
                    item = None

            element.clear()
            while element.getprevious() is not None:
                del element.getparent()[0]
        del iterparser

    def parse(self):
        for item in self.iterparser():
            pass
