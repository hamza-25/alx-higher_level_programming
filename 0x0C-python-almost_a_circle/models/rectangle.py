#!/usr/bin/python3
"""define rectangle class"""

from models.base import Base


class Rectangle(Base):
    """representation of rectangle
        take inherit from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle class
            Args:
                width: width of rectangle
                height: height of rectangle
                x: int number
                y: int  number
                id: id of objt
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__height = height
        self.__width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """representation of func that set width"""

        return self.__width

    @width.setter
    def width(sefl, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """representation of func that set height"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """representation of func that set x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """representation of func that set y"""

        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """representation of func that calculate area"""
        return self.width * self.height

    def display(self):
        """representation of func that disply area"""

        for line in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """representation of rectangle usign #"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
               )

    def update(self, *args, **kwargs):
        """representation of func tha update value of rectangle"""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.__width = arg
                elif index == 2:
                    self.__height = arg
                elif index == 3:
                    self.__x = arg
                elif index == 4:
                    self.__y = arg
                index += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """representation of a rectangle (to_dictionary) Return dict"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
