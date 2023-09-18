#!/usr/bin/python3
"""define Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """square inintialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """func that set size of square"""
        return self.__width

    @size.setter
    def size(self, value):
        #if not isinstance(value, int):
         #   raise TypeError("size must be an integer")
        #if value <= 0:
         #   raise ValueError("size must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """func that print info about suqare"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
