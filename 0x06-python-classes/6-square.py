#!/usr/bin/python3

"""define class Square."""


class Square:
    """Represent of square."""
    def __init__(self, size=0, position=(0, 0)):
        """init function ran every time we create an object.

         Args:
            size (int): square size.
            position (int, int): The square position.


        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the value of private attrb size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method that return current square area."""
        result = self.__size * self.__size
        return (result)

    def my_print(self):
        """porperty that print char before #."""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                print(" " * (self.__position[0]), end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
