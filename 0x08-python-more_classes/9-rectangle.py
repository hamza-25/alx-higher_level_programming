#!/usr/bin/python3
"""define Rectangle module."""


class Rectangle():
    """define rectangle class

    Attributes:
        number_of_instances (int): The number of each new Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init function."""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """__str__ print the rectangle with the character #."""
        shape = ""
        if self.__width == 0 or self.__height == 0:
            return shape
        for h in range(self.__height):
            for w in range(self.__width):
                shape += ("".join(str(self.print_symbol)))
            if not (h + 1) == self.__height:
                shape += "\n"
        return shape

    def __repr__(self):
        """__repr__ official represesntation"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """delete object"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            rect_2

    @classmethod
    def square(cls, size=0):
        """function that return same width and height

            Args:
                size (int): int value to assign width and height
        """
        return cls(size, size)
