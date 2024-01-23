#!/usr/bin/env python3

# Write a function that takes in a non-empty list of non-empty strings and returns a
# list of characters that are common to all strings in the list, ignoring multiplicity.

# Note that the strings are not guaranteed to only contain alphanumeric characters.
# The list you return can be in any order.


def commonCharacters(strings):
    lengthOfStrings = len(strings)

    if lengthOfStrings == 1:
        return list(strings[0])

    dataString = strings[0]
    commonChars = set(dataString) # space: O(c)
    output = set()

    for i in range(lengthOfStrings):  # time: O(n * m) 
        for char in list(commonChars):
            if char not in set(strings[i]):
                commonChars.remove(char)

    return list(commonChars)


if __name__ == "__main__":
    assert (commonCharacters(["abc", "bcd", "cbacca"])) == ["b", "c"]
