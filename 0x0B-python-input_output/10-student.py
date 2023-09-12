#!/usr/bin/python3
"""defines a class Student."""


class Student:
    """represent a student."""

    def __init__(self, f_name, l_name, age):
        """Initialize new student.
        """
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation student.
        """
        if (type(attrs) is list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
