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
        self.nodes = []
        self.checked = []
        for x in range(nodes):
            self.nodes.append(Node(x))
            
        for link in links:
            self.nodes[link[0]-1].add_link(self.nodes[link[1]-1])
            self.nodes[link[1]-1].add_link(self.nodes[link[0]-1])

    def print_all(self):
        for node in self.nodes:
            print '%d -> ' % node.id,
            for neighbor in node.neighbors:
                print '%d ' % neighbor.id,
            print
                
    def bfs(self, start, end, steps, checked, to_check, path):
        path = []
        checked.append(start)
        counter = 0
        ans = 0
        print start, 
        for node in self.nodes[start].neighbors:
            print node.id,
            if node.id not in checked:
                counter += 1
                checked.append(node.id)
                to_check.append(node.id)
                if node.id == end:
                    ans = steps
        print
        if counter == 0:
            return counter
#        for node in self.nodes[start].neighbors:
#            ans += self.bfs(node.id, end, steps+1, checked)
        for node in to_check:
            to_check.remove(node)
            ans += self.bfs(node, end, steps+1, checked, to_check, path)
        if ans:
            path.append(start)
            return ans
        else:
            return 0


