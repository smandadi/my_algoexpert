#!/usr/bin/env python3

# Write a function that takes in an array of integers and returns a sorted version of that array.
# Use the Selection Sort algorithm to sort the array.

# If you're unfamiliar with Selection Sort, we recommend watching the Conceptual Overview section of
# this question's video explanation before starting to code.

# time: O(n^2) | space O(1)
def selectionSort(array):
    currentIdx = 0
    l = len(array)
    
    while currentIdx < l - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx+1, l):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
        currentIdx += 1

    return array


if __name__ == "__main__":
    assert selectionSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
