#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """student Representation"""

    def __init__(self, f_name, l_name, age):
        """Initialize new Student.
        """
        self.f_name = first_name
        self.l_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation."""
        return self.__dict__
