#!/usr/bin/python3
""" module to validate UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding """
    bytes_remaining = 0
    for item in data:
        if not isinstance(item, int):
            return False
        if bytes_remaining == 0:
            if item & 0b10000000 == 0:
                bytes_remaining = 0
            elif item & 0b11100000 == 0b11000000:
                bytes_remaining = 1
            elif item & 0b11110000 == 0b11100000:
                bytes_remaining = 2
            elif item & 0b11111000 == 0b11110000:
                bytes_remaining = 3
            else:
                return False
        else:
            if item & 0b11000000 != 0b10000000:
                return False
            bytes_remaining -= 1
    return bytes_remaining == 0
