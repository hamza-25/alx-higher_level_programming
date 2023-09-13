#!/usr/bin/python3
"""defines object attribute lookup function
"""


def lookup(obj):
    """list of an object's available attributes.
    """
    return (dir(obj))
