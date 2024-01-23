#!/usr/bin/env python3

# The distance between a node in a Binary Tree and the tree's root is called the node's depth.

# Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

# Each BinaryTree node has an integer value, a left child node, and a right child node.
# Children nodes can either be BinaryTree nodes themselves or None / null.


class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def nodeDepthsRecurssive(tree, depth = 0):
    if tree is None:
        return 0
    return depth + nodeDepthsRecurssive(tree.left, depth + 1) + nodeDepthsRecurssive(tree.right, depth + 1)


def nodeDepthsIter(tree):

    data_stack = [{"node": tree, "depth": 0}]
    totalSum = 0

    while len(data_stack) > 0:
        node = data_stack.pop()
        if node["node"] is None:
            continue
        totalSum += node["depth"]
        data_stack.append({"node": node["node"].left, "depth": node["depth"]+1})
        data_stack.append({"node": node["node"].right, "depth": node["depth"]+1})

    return totalSum

if __name__ == "__main__":
    tree = BinaryTree(10, BinaryTree(5, BinaryTree(2, BinaryTree(1)), BinaryTree(6)), BinaryTree(15, BinaryTree(13, None, BinaryTree(14)), BinaryTree(22)))
    assert nodeDepthsRecurssive(tree) == 16, "This works!!!"
    assert nodeDepthsIter(tree) == 16, "even thsi works!!!"