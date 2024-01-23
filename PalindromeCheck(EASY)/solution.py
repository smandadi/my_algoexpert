#!/usr/bin/env python3

# Write a function that takes in a non-empty string and that returns a boolean
# representing whether the string is a palindrome.

# A palindrome is defined as a string that's written the same forward and backward.
# Note that single-character strings are palindromes.


# time O(n) and space O(1)
def isPalindrome(string):
    length = len(string) - 1
    start = 0

    while start < length:
        if string[start] != string[length]:
            return False
        start += 1
        length -= 1
    return True


if __name__ == "__main__":
    assert isPalindrome("abcdcba")
    assert not isPalindrome("abb")
