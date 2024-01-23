#!/usr/bin/env python3

# Write a function that takes in an array of integers and returns a sorted version of that array.
# Use the Bubble Sort algorithm to sort the array.

# If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual Overview section of
# this question's video explanation before starting to code.


# time: O(n^2) | space: O(1)
def bubbleSort(array):
    isSorted = False
    counter = 0
    
    while not isSorted:
        isSorted = True
        for idx in range(len(array) - 1 - counter):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx+1] = array[idx+1], array[idx]
                isSorted = False
        counter += 1

    return array


if __name__ == "__main__":
    assert bubbleSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]