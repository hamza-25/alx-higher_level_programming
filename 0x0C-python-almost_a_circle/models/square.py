#!/usr/bin/python3
"""define Square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        '''if value <= 0:
            raise ValueError("size must be > 0")
        if not isinstance(value, int):
            raise TypeError("size must be an integer")'''
        self.__width = value
        self.__height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
