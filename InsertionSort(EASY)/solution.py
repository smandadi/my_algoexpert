#!/usr/bin/env python3

# Write a function that takes in an array of integers and returns a sorted version of that array.
# Use the Insertion Sort algorithm to sort the array.

# If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual Overview section
# of this question's video explanation before starting to code.


# time: O(n^2) and space O(1)
def insertionSort(array):
    l = len(array)

    for idx in range(1, l):
        new_idx = idx
        while new_idx > 0 and array[new_idx] < array[new_idx -1]:
            array[new_idx], array[new_idx-1] = array[new_idx-1], array[new_idx]
            new_idx -= 1

    return array


if __name__ == "__main__":
    assert insertionSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]