#!/usr/bin/env python3

# You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.
# Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values.
# The Linked List should be modified in place (i.e., you shouldn't create a brand new list), and the modified Linked List should still have its nodes sorted with respect to their values.

# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null if it's the tail of the list.


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def printLinkedList(node):
    currentNode = node
    while currentNode is not None:
        print(currentNode.value, end=" -> ")
        currentNode = currentNode.next
    print(None)


def removeDuplicatesFromLinkedList(node):

    currentNode = node

    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
        currentNode = nextNode
    
    return node


if __name__ == "__main__":
    node = Node(1, Node(1, Node(3, Node(4, Node(4, Node(4, Node(5, Node(6, Node(6)))))))))
    out_node = Node(1, Node(3, Node(4, Node(5, Node(6)))))
    printLinkedList(out_node)
    printLinkedList(removeDuplicatesFromLinkedList(node))
