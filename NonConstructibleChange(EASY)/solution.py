#!/usr/bin/env python3

# Given an array of positive integers representing the values of coins
# in your possession, write a function that returns the minimum amount
# of change (the minimum sum of money) that you cannot create. The
# given coins can have any positive integer value and aren't necessarily
# unique(i.e you can have multiple coins of the same value).

# For example, if you're given coins = [1, 2, 5], the minimum amount of change
# that you can't create is 4. If you're given no coins, the minimum amount of
# change that you can't create is 1.

# space = o(1)
# time = o(nlogn)
def nonConstructibleChange(coins):
    length = len(coins)

    if length < 1:
        return 1
    elif length == 1 and coins[0] != 1:
        return 1

    coins = coins.sort()
    totalSum = coins[0]

    for i in range(1, length):
        if totalSum < coins[i] and (coins[i] - totalSum) != 1:
            return totalSum + 1
        elif totalSum >= coins[i] or (coins[i] - totalSum) == 1 :
            totalSum += coins[i]
    return totalSum + 1