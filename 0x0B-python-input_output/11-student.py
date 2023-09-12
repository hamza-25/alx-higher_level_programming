#!/usr/bin/python3
"""refines a class Student."""


class Student:
    """represent student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        """
        self.f_name = first_name
        self.l_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        """
        if (type(attrs) is list and
                all(type(elem) is str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes.
        """
        for k, v in json.items():
            setattr(self, k, v)
