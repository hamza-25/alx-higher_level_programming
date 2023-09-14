#!/usr/bin/python3
"""defines a rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square."""

    def __init__(self, size):
        """new square Initializition.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
