#!/usr/bin/env python3

# The Fibonacci sequence is defined as follows: the first number of the sequence is 0
# ,the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. 
# Write a function that takes in an integer and returns the nth Fibonacci number.
# Important note: the Fibonacci sequence is often defined with its first two numbers as F(0) = 0
# F(1) = 1. For the purpose of this question, the first Fibonacci number is
# and
# FO; therefore,
# getNthFib(1)] Is equal to
# FO, getNthFib(2) Is equal to F1, etc..


# Time: O(n)
# Space = O(1)
def getNthFib(n):

    if n <= 1:
        return 0

    result = [0, 1] # n = 1, 2

    for i in range(2, n):
        result = [result[1], result[0] + result[1]]

    return result[1]


if __name__ == "__main__":
    assert 5 == getNthFib(6), "this should work."
    assert 6 == getNthFib(6), "this shouldn't work."