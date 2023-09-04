#!/usr/bin/python3
"""define Rectangle module."""


class Rectangle():
    """define rectangle class."""

    def __init__(self, width=0, height=0):
        """init function."""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width func that set the height."""
        return self.__width

    @width.setter
    def width(self, value):
        """width func that set the height."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height func that set the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """height func that set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
