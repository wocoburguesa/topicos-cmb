from pprint import pprint

from poisson import *

class Node(object):

    def __init__(self, _id):
        self.id = _id
        self.neighbors = []
        self.packages = 0

    def add_link(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def add_package(self):
        self.packages += 1

    def remove_package(self):
        self.packages -= 1

    def __str__(self):
        return "<NODE ID=%d PACKAGES=%d>" % \
            (self.id, self.packages)

class Package(object):
    def __init__(self, origin, destination, path):
        self.current = origin
        self.destination = destination
        self.path = path

    def __str__(self):
        return "<PACKAGE CURRENT_POS=%d DESTINATION=%d>" % (
            self.current+1, self.destination+1)

class Network(object):

    def __init__(self,
                 nodes,
                 links,
                 lamb):
        self.poisson = Poisson()
        self.poisson.make_distribution(lamb)

        self.nodes = []
        self.checked = []
        for x in range(nodes):
            self.nodes.append(Node(x))

        for link in links:
            self.nodes[link[0]-1].add_link(self.nodes[link[1]-1])
            self.nodes[link[1]-1].add_link(self.nodes[link[0]-1])

        self.packages = []
        self.generate_packages()

    def step(self):
        for pack in self.packages:
            if len(pack.path) == 0:
                self.nodes[pack.current].remove_package()

        self.packages = filter(lambda a: len(a.path) != 0, self.packages)

        for pack in self.packages:
            self.nodes[pack.current].remove_package()
            pack.current = pack.path.pop()
            self.nodes[pack.current].add_package()

        for pack in self.packages:
            print pack
            print [x+1 for x in pack.path]
            self.nodes[pack.current].add_package()
        self.generate_packages()

    def generate_packages(self, lamb=None):
        if lamb:
            self.poisson = Poisson()
            self.poisson.make_distribution(lamb)

        for i in range(self.poisson.generate()):
            origin = random.randint(0, len(self.nodes)-1)
            destination = random.randint(0, len(self.nodes)-1)
            while origin == destination:
                destination = random.randint(0, len(self.nodes)-1)
            path = self.make_path(origin, destination)
            path.pop()
            self.nodes[origin].add_package()
            self.packages.append(Package(origin, destination, path))

    def make_path(self, start, end):
        return self.bfs(start, end, {start: -1}, [])

    def path_from_dict(self, checked, start):
        path = [start]
        while checked[start] != -1:
            path.append(checked[start])
            start = checked[start]
        return path

    def bfs(self, start, end, checked, to_check=None):
        if not to_check:
            to_check = []
        counter = 0
        for node in self.nodes[start].neighbors:
            if node.id not in checked.keys():
                counter += 1
                checked[node.id] = start
                if node.id not in to_check:
                    to_check.append(node.id)
                if node.id == end:
                    return self.path_from_dict(checked, start)

        if counter == 0:
            return None

        for i in range(len(to_check)):
            next_ = to_check.pop(0)
            res = self.bfs(next_, end, checked, to_check)
            if res:
                return res

    def __str__(self):
        string =  "<NETWORK>\n"
        for node in self.nodes:
            string += "%s\n" % node.__str__()
        string += "</NETWORK>"
        return string
