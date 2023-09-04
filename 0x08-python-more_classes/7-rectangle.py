#!/usr/bin/python3
"""define Rectangle module."""


class Rectangle():
    """define rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init function."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """calculate the area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """calculate the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """__str__ print the rectangle with the character #."""
        shape = ""
        if self.width == 0 or self.height == 0:
            return shape
        for h in range(self.height):
            for w in range(self.width):
                shape += Rectangle.print_symbol
            if not (h + 1) == self.height:
                shape += "\n"
        return shape

    def __repr__(self):
        """__repr__ official represesntation"""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """delete object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
