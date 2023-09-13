#!/usr/bin/python3
"""defines a class-checking function."""


def is_same_class(obj, a_class):
    """check object matching class.

    Args:
        obj : object check.
        a_class : class to match with objt.
    Returns:
        if match - True.
        Otherwise - False.
    """
    if type(obj) is not a_class:
        return False
    return True
