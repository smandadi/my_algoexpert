#!/usr/bin/env python3

# Given a non-empty string of lowercase letters and a non-negative integer representing a key,
# write a function that returns a new string obtained by shifting every letter in the input string
# by k positions in the alphabet, where k is the key.

# Note that letters should "wrap" around the alphabet; in other words, the letter 2 shifted by one
# returns the letter

# time: O(n), space: O(n) = (o(26) + o(26) + o(n))
def caesarCipherEncryptor(string, key):
    alpha_list = list("abcdefghijklmnopqrstuvwxyz")
    alpha_dict = {k:v for v,k in enumerate(alpha_list)}
    result = []

    for c in string:
        new_key = alpha_dict[c] + key
        if new_key > 25:
            new_key = new_key % 26
        result.append(alpha_list[new_key])

    return "".join(result)


if __name__ == "__main__":
    assert caesarCipherEncryptor("xyz", 25) == "wxy"
