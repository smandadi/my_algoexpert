#!/usr/bin/env python3

# Write a function that takes in an array of at least three integers and,
# without sorting the input array, returns a sorted array of the three largest integers in the input array.
# The function should return duplicate integers if necessary; for example, it should return [10, 10, 12]
# for an input array of [10, 5, 9, 10, 12].


# time: O(n), space = O(1)
def findThreeLargestNumbers(array):

    result = [-float('inf'), -float('inf'), -float('inf')]

    for num in array:
        if num > result[2]:
            result = [result[1], result[2], num]
        elif num > result[1]:
            result = [result[1], num, result[2]]
        elif num > result[0]:
            result = [num, result[1], result[2]]

    return result


if __name__ == "__main__":
    assert findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]) == [18, 141, 541]
