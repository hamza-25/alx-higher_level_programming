#!/usr/bin/python3

"""define an empty class Square."""


class Square:
    """Represent of square."""
    def __init__(self, size=0):
        """init function ran every time we create an object."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
