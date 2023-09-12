#!/usr/bin/python3
"""file-appending function."""


def append_write(filename="", text=""):
    """Appends a string.

    Returns:
        number of characters.
    """
    with open(filename, "a", encoding="utf-8"):
        return open(filename, "a", encoding="utf-8").write(text)
