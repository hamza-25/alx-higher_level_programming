#!/usr/bin/python3
"""define locked class"""


class LockedClass:
    """representaion LockedClass
    prevents the user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name
    """
    __solts__ = ["first_name"]
