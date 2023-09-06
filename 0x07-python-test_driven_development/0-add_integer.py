#!/usr/bin/python3
"""
implmt addition function

"""


def add_integer(a, b=98):

    """
    add two integer and return sum.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return sum
