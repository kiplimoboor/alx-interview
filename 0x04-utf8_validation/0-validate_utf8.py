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

    for byte in data:
        if count == 0:
            if byte >> 5 == 0b00000110:
                count = 1
            elif byte >> 4 == 0b00001110:
                count = 2
            elif byte >> 3 == 0b00011110:
                count = 3
            elif byte >> 7 != 0b00000000:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            count -= 1

    return count == 0
