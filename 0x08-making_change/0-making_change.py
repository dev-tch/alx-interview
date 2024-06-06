#!/usr/bin/python3
""" module with one function """


def makeChange(coins, total):
    """ determine the fewest number of coins
    needed to meet a given amount total"""
    if total <= 0:
        return 0
    # choose value  biggest that total it can be INFINITY
    # or any random big NUMBER > total
    # initialize array of size(total + 1) with choosed MAX value
    # init index 0 with 0 : cause with amount 0 we have 0 coins
    size = (total + 1)
    MAXNUMBER = total + 1
    U = [MAXNUMBER] * size
    U[0] = 0

    for n in range(1, size):
        for c in coins:
            if n - c >= 0:
                U[n] = min(U[n], U[n - c] + 1)
    return U[total] if U[total] != MAXNUMBER else -1
