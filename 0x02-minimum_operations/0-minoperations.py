#!/usr/bin/python3
""" module with one function def minOperations"""


def minOperations(n):
    """ calculates the fewest number of operations
    needed to result in exactly n H characters in the file"""
    old_text = 'H'
    text = 'H'
    min_op = 0
    while (len(text) < n):
        if n % len(text) == 0:
            min_op += 2
            old_text = text
            text += text
        else:
            min_op += 1
            text += old_text
    if len(text) != n:
        return 0
    return min_op
