#!/usr/bin/python3
""" module with one function """
import math


def makeChange(coins, total):
    """ determine the fewest number of coins
    needed to meet a given amount total"""
    if total <= 0:
        return 0
    # choose value  biggest that total it can be INFINITY
    # let say math.inf > total
    # initialize array of size(total + 1) with choosed MAX value
    # init index 0 with 0 : cause with amount 0 we have 0 coins
    size = (total + 1)
    U = [math.inf] * size
    U[0] = 0

    for n in range(1, size):
        U[n] = min(U[n - c] + 1 if n - c >= 0 else math.inf
                   for c in coins)
    return U[total] if U[total] != math.inf else -1
