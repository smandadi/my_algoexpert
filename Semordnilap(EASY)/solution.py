#!/usr/bin/env python3

# Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.
# A semordnilap pair is defined as a set of different strings where the reverse of one word is the
# same as the forward version of the other. For example the words "diaper" and "repaid" are a
# semordnilap pair, as are the words "palindromes" and "semordnilap".

# The order of the returned pairs and the order of the strings within each pair does not matter.


# time: O(n * m) | space: O(n * m)
def semordnilap(words):
    output = []
    words_set = set(words)
    for word in words:
        reverse = word[::-1]
        if reverse in words_set and reverse != word:
            output.append([word, reverse])
            words_set.remove(word)
            words_set.remove(reverse)

    return output


if __name__ == "__main__":
    assert(semordnilap(["dog", "hello", "desserts", "test", "god", "stressed"])) == [['dog', 'god'], ['desserts', 'stressed']]