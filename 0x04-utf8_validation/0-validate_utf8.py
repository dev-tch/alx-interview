#!/usr/bin/python3
""" module to validate UTF-8 encoding"""


def leading_ones_cpt(data):
    """ count leading ones"""
    for i in range(8):
        if data >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
            return i
    return 8


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding """
    data = iter(data)
    for byte in data:
        cpt_lead_ones = leading_ones_cpt(byte)
        if cpt_lead_ones in [1, 7, 8]:
            return False
        for _ in range(cpt_lead_ones - 1):
            next_byte = next(data, None)
            if next_byte is None or next_byte >> 6 != 0b10:
                return False
    return True
