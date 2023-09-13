#!/usr/bin/python3
"""defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing list class."""

    def print_sorted(self):
        """print list stored"""
        print(sorted(self))
