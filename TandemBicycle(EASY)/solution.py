#!/usr/bin/env python3

# A tandem bicycle is a bicycle that's operated by two people: person A and person B.
# Both people pedal the bicycle, but the person that pedals faster dictates the speed
# of the bicycle. So if person A pedals at a speed of 5, and person B pedals at a speed
# of 4, the tandem bicycle moves at a speed of 5 (i.e., tandemSpeed = max (speedA, speedB)).

# You're given two lists of positive integers: one that contains the speeds of riders wearing
# red shirts and one that contains the speeds of riders wearing blue shirts. Each rider is
# represented by a single positive integer, which is the speed that they pedy! a tandem bicycle at.
# Both lists have the same length, meaning that there are as many red-shirt riders as there are blue-shirt riders.
# Your goal is to pair every rider wearing a red shirt with a rider wearing a blue shirt to operate a tandem bicycle.

# Write a function that returns the maximum possible total speed or the minimum possible total speed of all of
# the tandem bicycles being ridden based on an input parameter, fastest. If fastest = true, your
# function should return the maximum possible total speed; otherwise it should return the minimum total speed.
# "Total speed" is defined as the sum of the speeds of all the tandem bicycles being ridden. For example, 
# if there are 4 riders (2 red-shirt riders and 2 blue-shirt riders) who have speeds of 1, 3, 4, 5, and 
# if they're paired on tandem bicycles as follows: [1, 4], [5, 31, then the total speed of these tandem bicycles is
# 4 + 5 = 9.


# time: O(nlog(n)) | space: O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort(reverse=fastest)
    blueShirtSpeeds.sort()
    result = 0

    for r, b in zip(redShirtSpeeds, blueShirtSpeeds):
        result += max(r, b)
        
    return result


if __name__ == "__main__":
    assert(tandemBicycle([3, 6, 7, 2, 1], [5, 5, 3, 9, 2], True)) == 32
    