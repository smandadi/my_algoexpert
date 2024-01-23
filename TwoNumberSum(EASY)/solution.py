#!/usr/bin/env python3

# TwoNumberSum

# Write a fucntion that takes in a non-empty array of distinct integers and an # integer
# representing a target sum. If any two numbers in the input array sum up to the target
# sum, the function should return them in an array, in any order. If no two numbers sum
# up to the target sum, the function should return an empty array.
# Note that the target sum has to be obtained by summing two different integers in the array;
# you can't add a single integer to itself in order to obtain the target sum.

# You can assume that there will be at most one pair of numbers summing up the target sum.

# Sample Output:
#
# array = [3. 5. -4, 8, 11, 1, -1, 6]
# targetSum = 10


def twoNumberSum(array, targetSum):
    cacheData = []

    for i in array:
        _tmp = targetSum - i
        if _tmp in cacheData:
            return [i, _tmp]
        cacheData.append(i)
    return []