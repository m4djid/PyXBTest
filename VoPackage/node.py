class Vospace(object):
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def findNodes(self, target):
        self.target = target
        if self.target in Node:
            return self.target

    def listNodes(self):
        return self.nodes

    def createNode(self, node):
        self.node = node
        pass

class Capability(object):
    def __init__(self, uri, endpoint, param):
        self.uri = uri
        self.endpoint = endpoint
        self.param = param

class Property(object):
    def __init__(self, uri, value, readonly):
        self.uri = uri
        self.value = value
        self.readonly = readonly

class Node(object):
    def __init__(self, uri):
        self.uri = uri
        self.properties = []
        self.capabilities = []

    def add_property(self, property):
        self.properties.append(property)

    def add_capability(self, capability):
        self.capabilities.append(capability)

    def copyNode(self, node, folder):
        self.node = node
        self.folder = folder
        pass

    def moveNode(self, node, folder):
        self.node = node
        self.folder = folder
        pass

    def deleteNode(self, node):
        self.node = node
        pass

class LinkNode(object):
    def __init__(self, target):
        self.target = target

class View(object):
    def __init__(self, uri, param, original):
        self.uri = uri
        self.param = param
        self.original = original

class DataNode(Node):
    def __init__(self, uri, busy):
        Node.__init__(self, uri)
        self.accepts = []
        self.provides = []
        self.busy = busy

    def add_accept_view(self,view):
        self.accepts.append(view)

    def add_provide_view(self,view):
        self.provides.append(view)

class ContainerNode(DataNode):
    def __init__(self, uri, busy):
        DataNode.__init__(self, uri, busy)

class UnstructuredDataNode(DataNode):
    def __init__(self, uri, busy):
        DataNode.__init__(self, uri, busy)

class StructuredDataNode(DataNode):
    def __init__(self, uri, busy):
        DataNode.__init__(self, uri, busy)