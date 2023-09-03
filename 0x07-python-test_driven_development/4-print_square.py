#!/usr/bin/python3
"""define a square by #."""


def print_square(size):
    """function that print square
        Args:
            @size: required number int 
        Errors:
            TypeError, ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for col in range(size):
        for row in range(size):
            print("#", end="")
        print("")
