#!/usr/bin/env python3

# Write a function that takes in a string of lowercase English-alphabet letters and
# returns the index of the string's first non-repeating character.

# The first non-repeating character is the first character in a string that occurs only once.
# If the input string doesn't have any non-repeating characters, your function should return
# -1.


def firstNonRepeatingCharacter(string):

    dups = {}

    for i in string:
        if i not in dups:
            dups[i] = 1
        else:
            dups[i] += 1

    for i,l in enumerate(string):
        if dups[l] == 1:
            return i

    return -1


if __name__ == "__main__":
    assert firstNonRepeatingCharacter("abcdcaf") == 1