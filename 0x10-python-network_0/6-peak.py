#!/usr/bin/python3
"""define module peak function"""


def find_peak(list_of_integers):
    """representation of a peak function"""
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    rev = list_of_integers[0]
    for i in range(1, length):
        if list_of_integers[i] > rev:
            rev = list_of_integers[i]
    return rev

