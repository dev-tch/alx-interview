#!/usr/bin/python3
""" module to validate UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding """
    lent_byte = 0
    for item in data:
        if not isinstance(item, int):
            return False
        if lent_byte == 0:
            if item >> 5 == 0b110:
                lent_byte = 1
            elif item >> 4 == 0b1110:
                lent_byte = 2
            elif item >> 3 == 0b11110:
                lent_byte = 3
            elif item >> 7 != 0:
                return False
        else:
            if item >> 6 != 0b10:
                return False
            lent_byte -= 1
    return (lent_byte == 0)
