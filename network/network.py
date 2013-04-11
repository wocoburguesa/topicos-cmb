class Node(object):
    
    def __init__(self, _id):
        self.id = _id
        self.neighbors = []
    
    def add_link(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

class Network(object):

    def __init__(self,
                 nodes,
                 links):
        self.nodes = [Node(x) for x in range(nodes)]
        for link in links:
            self.nodes[link[0]].add_link(link[1])
            self.nodes[link[1]].add_link(link[0])
