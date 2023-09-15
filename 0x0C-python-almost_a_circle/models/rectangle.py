#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id=None)

    @property
    def set_width(self):
        return self.__width
    
    @set_width.setter
    def set_width(sefl, width):
        self.__width = width
    
    @property
    def set_height(self):
        return self.__height
    
    @set_height.setter
    def set_height(sefl, height):
        self.__height = height
    
    @property
    def set_x(self):
        return self.__x

    @set_x.setter
    def set_x(sefl, x):
        self.__x = x

    @property
    def set_y(self):
        return self.__y

    @set_y.setter
    def set_y(sefl, y):
        self.__y = y

