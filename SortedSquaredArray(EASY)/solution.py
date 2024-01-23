#!/usr/bin/env python3

# Write a function that takes in a non-empty array of integers
# that are sorted in ascending order and returns a new array of
# the same length with the squares of the original integers also
# sorted in ascending order.

# space = O(n)
# time = O(nlogn)

def sortedSquaredArray(array):
    m = [x*x for x in array]
    return sorted(m)


def sortedSquaredArray2(array):
    l = len(array)
    output = [0] * l
    
    # we know that array is sorted.
    largest = l - 1
    smallest = 0

    for i in reversed(range(l)):
        s = array[smallest]
        l = array[largest]

        if abs(s) > abs(l):
            output[i] = s*s
            smallest += 1
        else:
            output[i] = l*l
            largest -=1

    return output