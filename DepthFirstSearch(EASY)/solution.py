#!/usr/bin/env python3

# You're given a Node class that has a name nodes form an acyclic tree-like structure.
# and an array of optional children nodes. When put together, nodes form an acyclic tree like structure.

# Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the
# tree using the Depth-first Search approach (specifically navigating the tree from left to right), stores
# all of the nodes' names in the input array, and returns it.

# If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual Overview section of
# this question's video explanation before starting to code.


# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)

        for node in self.children:
            node.depthFirstSearch(array)

        return array


if __name__ == "__main__":
    A, B, C, D, E, F, G, H, I, J, K = Node('A'), Node('B'), Node('C'), Node('D'), Node('E'), Node('F'), Node('G'), Node('H'), Node('I'), Node('J'), Node('K')
    A.children = [B, C, D]
    B.children= [E, F]
    D.children = [G, H]
    F.children = [I, J]
    G.children = [K]

    assert A.depthFirstSearch([]) == ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']