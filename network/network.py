class Node(object):
    
    def __init__(self, _id):
        self.id = _id
        self.neighbors = []
    
    def add_link(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)
            node.neighbors.append(self)

class Network(object):

    def __init__(self,
                 nodes,
                 links):
        self.nodes = [Node(x) for x in range(nodes)]
        for link in links:
            self.nodes[link[0]].add_link(nodes[link[1]])
