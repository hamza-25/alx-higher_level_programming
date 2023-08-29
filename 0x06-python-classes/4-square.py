#!/usr/bin/python3

"""define an empty class Square."""


class Square:
    """Represent of square."""
    def __init__(self, size=0):
        """init function ran every time we create an object."""
        self.__size = size

    def area(self):
        """Method that return current square area."""
        result = self.__size * self.__size
        return (result)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_name):
        """get the value of private attrb size"""
        if type(new_name) is not int:
            raise TypeError("size must be an integer")
        if new_name < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_name
