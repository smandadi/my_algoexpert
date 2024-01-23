#!/usr/bin/env python3

# Write a function that takes in a sorted array of integers as well as a target integer.

# The function should use the Binary Search algorithm to determine if the target integer 
# is contained in the array and should return its index if it is, otherwise -1.
# If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview
# section of this question's video explanation before starting to code.

# time: O(log(n)) | space: O(1)
def binarySearchIter(array, target):

    end = len(array)
    start = 0

    while start < end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    
    return -1

# time: O(log(n)) | Space O(log(n))
def binarySearch(array, target):
    return binarySearchRecurssive(array, target, 0, len(array)-1)


def binarySearchRecurssive(array, target, start, end):

    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    
    if array[mid] > target:
        return binarySearchRecurssive(array, target, start, mid-1)
    elif array[mid] < target:
        return binarySearchRecurssive(array, target, mid+1, end)
    
    return -1


if __name__ == "__main__":
    assert binarySearchIter([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33) == 3, "This works!!!"
    assert binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33) == 3, "This works!!!"