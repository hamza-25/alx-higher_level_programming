#!/usr/bin/python3
"""defines Basegeometry class."""


class BaseGeometry:
    """base geometry representation."""

    def area(self):
        """raise error not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate int parameter.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
