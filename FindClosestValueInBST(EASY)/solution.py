#!/usr/bin/env python3

# Write a function that takes in a Binary Search tree (BST) and a target
# integer value and returns the closest value to that target value contained
# in the BST.

# You can assume that there will only be one closest value.

# Each BST node has a integer value, a left child node, and a right child
# node. A node is said to be a valid BST node if and only if it satisfies the
# BST property: its value is strictly greater than the values of every node to
# its left; its value is less than or equal to teh value of every node to its right;
# and its children nodes are either valid BSt nodes themselves or None / null.

# Average space = O(log(n)) and time = O(log(n))
# worst space = O(n) and time = O(n)

def findClosestValueInBst(tree, target):
    return findRecurssively(tree, target, tree.value)


def findRecurssively(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target > tree.value:
        return findRecurssively(tree.right, target, closest)
    elif target < tree.value:
        return findRecurssively(tree.left, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
