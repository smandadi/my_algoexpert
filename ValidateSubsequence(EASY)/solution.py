#!/usr/bin/env python3

# Given two non-empty arrays of integers, write a function that determines
# whether the second array is a subsequence of the firts one.

# A subsequence of an array is a set of numbers that aren't necessarily adjacent
# in the array but that are in the same order as they appear in the array. For
# instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4],
# and so do the numbers [2, 4]. Note that a single number in an array and itself
# are both valid subsequence of the array.

# space = O(n)
# time = O(n)

def isValidSubsequence(array, sequence):
    s_len = len(sequence)
    a_len = len(array)
    i = 0
    j = 0

    if s_len > a_len:
        return False

    while a_len > i:
        if array[i] == sequence[j]:
            i += 1
            j += 1
        else:
            i += 1
        if j == s_len:
            return True
    return False
