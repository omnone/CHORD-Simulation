class Finger_Entry:
    def __init__(self, start, node):
        self.start = start
        self.node = node

# Declaration of class : Node
class Node:

    def __init__(self, id, m):
        self.id = id
        self.successor = None
        self.predecessor = None
        self.data = {}
        self.finger_table = [Finger_Entry(
            (id + 2 ** k) % 2**m, self) for k in range(0, m)]

    def __repr__(self):
        print(f'Node with id:{self.id} , succ:{self.successor.id}')

      # Join node to network

    def join(self, node, network):
        print(f'[*] Node {self.id} tries to join network')
        self.predecessor = None
        self.successor = node.find_successor(self.id, network)
        print(f'[+]Successor found for node {self.id} is {self.successor.id}')

      # find the successor of a key or a node
    def find_successor(self, node_id, network):
        if network.distance(self.id, node_id) <= network.distance(self.finger_table[0].id, node_id):
            return self.successor
        else:
            n0 = self.closest_preceding_node(node_id, network)
            return n0.find_successor(node_id)

    # find the close preceding node of a key
    def closest_preceding_node(self, node_id, network):
        for i in range(network.m, 0, -1):
            if network.distance(self.finger_table[i].id, node_id) < network.distance(self.finger_table[i + 1].id, node_id):
                return self.finger_table[i]
        return self


# Declaration of class : Network
class Network:
    def __init__(self, m):
        self.m = m
        self.size = 2**m
        self._startNode = Node(0, m)
        self._startNode.finger_table[0] = self._startNode
        self._startNode.predecessor = self._startNode
        self._startNode.successor = self._startNode.finger_table[0]

    # Find distance between two nodes
    def distance(self, n1, n2):
        if n1 == n2:
            return 0
        if n1 < n2:
            return n2 - n1
        return self.size - n1 + n2


# def main():


# if __name__ == "__main__":
#     main()
