#!/usr/bin/python3

"""A simple UTF 8 validator"""


def validUTF8(data):
    """
    Checks if data input is a valid utf-8 entry
    Args:
        data: a list of integers
    Return:
        True if data is valid utf-8, False otherwise
    """

    count = 0

    for i in data:
        if count == 0:
            if i >> 7 != 0b0:
                return False

            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                count = 1
            elif i >> 4 == 0b1110:
                count = 2
            elif i >> 3 == 0b11110:
                count = 3
        else:
            if i >> 6 != 0b10:
                return False
            count -= 1

    return count == 0
