#!/usr/bin/env python3

# You're given a string of available characters and a string representing a document
# that you need to generate.

# Write a function that determines if you can generate the document using the available characters.
# If you can generate the document, your function should return true; otherwise, it should return false.
# You're only able to generate the document if the frequency of unique characters in the characters string
# is greater than or equal to the frequency of unique characters in the document string. For example, if you're
# given characters = "abcabc" and document = "aabbecc" you cannot generate the document
# because you're missing one c
# The document that you need to create may contain any characters, including special characters, capital letters,
# numbers, and spaces.

# Note: you can always generate the empty string ("")


# time = O(m + n) | space: O(m + n)
def generateDocument(characters, document):

    count_characters = counter(characters)
    count_document = counter(document)

    for k,v in count_document.items():
        if k not in count_characters or count_characters[k] < v:
            return False
    return True

def counter(word):

    count = {}

    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


if __name__ == "__main__":
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"
    assert generateDocument(characters, document)