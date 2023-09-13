#!/usr/bin/python3
"""define inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """check objt and class are instance.
        Return:
        true if check pass
        Otherwise - False.
    """
    if not (isinstance(obj, a_class)):
        return False
    return True
