#!/usr/bin/env python3

# You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List.
# If there are two middle nodes (i.e. an even length list), your function should return the second of these nodes.

# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to
# None / nu11
# if it's the tail of the list.


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# time O(n) | Space: O(n)
def middleNode(linkedList):
    nodes = []
    currentNode = linkedList

    while currentNode is not None:
        nodes.append(currentNode)
        currentNode = currentNode.next
    return nodes[len(nodes)//2]


# time O(n) | space O(1)
def middleNode2(linkedList):
    count = 0
    currentNode = linkedList

    while currentNode is not None:
        count += 1
        currentNode = currentNode.next

    middleNode = linkedList
    for _ in range(count//2):
        middleNode = middleNode.next

    return middleNode


# time: O(n) | space O(1)
def middleNode3(linkedList):

    slowNode = linkedList
    fastNode = linkedList

    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode


if __name__ == "__main__":
    node = LinkedList(2, LinkedList(7, LinkedList(3, LinkedList(4))))
    assert middleNode(node) == node.next.next
    assert middleNode2(node) == node.next.next
    assert middleNode3(node) == node.next.next
