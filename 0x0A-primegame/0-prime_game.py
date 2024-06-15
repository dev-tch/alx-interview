#!/usr/bin/python3
"""
module for computing game prime
"""


def play_round(n, primes, db):
    """
    logic for one round playing
    """
    selection = set(range(1, n + 1))
    turn = 0
    for p in primes:
        if p in selection:
            selection -= {p * k for k in range(1, (n // p) + 1)}
            turn = 1 - turn
    if turn == 0:
        db['Ben'] += 1
    else:
        db['Maria'] += 1


def erasto(n):
    """
    return list primes lower than n
    """
    primes = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (primes[p]):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    lst = list(filter(lambda x: primes[x], range(2, n + 1)))
    return lst


def isWinner(x, nums):
    """
    return the name of winner
    """
    db = {'Maria': 0, 'Ben': 0}
    primes = erasto(max(nums))
    for n in nums:
        play_round(n, primes, db)
    if db['Maria'] > db['Ben']:
        return 'Maria'
    elif db['Ben'] > db['Maria']:
        return 'Ben'
    else:
        return None
