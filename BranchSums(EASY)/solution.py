#!/usr/bin/env python3

# Write a function that takes in a Binary Tree and returns a list of its
# branch sums ordered from left most branch sum to rightmost branch sum.

# A branch sum is the sum of all values in a Binary Tree branch. 
# A Binary Tree branch is a path of nodes in a tree that starts
# at the root node and ends at any leaf node.

# Each BinaryTree node has an integer value, a left child node, and a right
# child node.Children nodes can either be BinaryTree nodes themselves or None/null.


class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def branchSum(tree):
    totalSums = []
    branchSumRecurssion(tree, 0, totalSums)
    return totalSums


def branchSumRecurssion(tree, currentSum, totalSums):

    if tree is None:
        return
    
    newSum = currentSum + tree.value
    if tree.left is None and tree.right is None:
        totalSums.append(newSum)
        return
    
    branchSumRecurssion(tree.left, newSum, totalSums)
    branchSumRecurssion(tree.right, newSum, totalSums)


if __name__ == "__main__":
    tree = BinaryTree(10, BinaryTree(5, BinaryTree(2, BinaryTree(1)), BinaryTree(6)), BinaryTree(15, BinaryTree(13, None, BinaryTree(14)), BinaryTree(22)))
    assert branchSum(tree) == [18, 21, 52, 47], "This works!!!"
