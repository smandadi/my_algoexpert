#!/usr/bin/env python3

# Write a function that takes in a non-empty string and returns its run-length encoding.
# From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of
# data are stored as a single data value and count, rather than as the original run." For this
# problem, a run of data is any sequence of consecutive, identical characters. So the run "AAA"
# would be run-length-encoded as "3A".
# To make things more complicated, however, the input string can contain all sorts of special characters,
# including numbers. And since encoded data must be decodable, this means that we can't naively run-length-encode
# long runs. For example, the run "AAAAAAAAAAAA" (12 A s), can't naively be encoded as "12A", since this string
# can be decoded as either "AAAAAAAAAAAA" or "1AA". Thus, long runs (runs of 10 or more characters) should be encoded
# in a split fashion; the aforementioned run should be encoded as "9A3A".


# time: O(n) and Space O(n)
def runLengthEncoding(string):

    result = ""
    l = len(string)
    start = 0
    count = 0
    prev = string[0]

    while start < l: # o(n) | space: O(n)
        char = string[start]
        if count < 9 and char == prev:
            count += 1
            prev = char
        elif count == 9:
            result += f"9{prev}"
            count = 1
            prev = char
        elif char != prev:
            result += f"{str(count)}{prev}"
            prev = char
            count = 1
        if start == l - 1:
            result += f"{str(count)}{char}"
        start += 1

    return result


if __name__ == "__main__":
    assert runLengthEncoding("........______=========AAAA   AAABBBB   BBB") == "8.6_9=4A3 3A4B3 3B"