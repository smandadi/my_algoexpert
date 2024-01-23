#!/usr/bin/env python3

# You're given a binary expression tree. Write a function to evaluate this tree mathematically
# and return a single resulting integer.
# All leaf nodes in the tree represent operands, which will always be positive integers.
# All of the other nodes represent operators. There are 4 operators supported, each of which
# is represented by a negative integer:
# -1: Addition operator, adding the left and right subtrees.
# -2: Subtraction operator, subtracting the right subtree from the left subtree.
# -3: Division operator, dividing the left subtree by the right subtree. If the result is a decimal,
# it should be rounded towards zero.
# -4: Multiplication operator, multiplying the left and fight subtrees.

# You can assume the tree will always be a valid expression tree. Each operator also works as
# a grouping symbol, meaning the bottom of the tree is always evaluated first, regardless of the operator.

class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressTree(tree):

    if tree.value >= 0:
        return tree.value

    leftNode = evaluateExpressTree(tree.left)
    rightNode = evaluateExpressTree(tree.right)

    if tree.value == -1:
        return (leftNode + rightNode)
    elif tree.value == -2:
        return (leftNode - rightNode)
    elif tree.value == -3:
        return int(leftNode / rightNode)
    else:
        return (leftNode * rightNode)


if __name__ == "__main__":
    tree = BinaryTree(-1, BinaryTree(-2, BinaryTree(-4, BinaryTree(2), BinaryTree(3)), BinaryTree(2)), BinaryTree(-3, BinaryTree(8), BinaryTree(3)))
    print(evaluateExpressTree(tree))
    assert evaluateExpressTree(tree) == 6, "This works!!!"
