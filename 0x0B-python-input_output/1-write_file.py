#!/usr/bin/python3
"""file-writing function."""


def write_file(filename="", text=""):
    """Write a string.

    Args:
        filename (str): The name of the file.
        text (str): txt to write.
    Returns:
        int num of char
    """
    with open(filename, "w", encoding="utf-8"):
        return open(filename, "w", encoding="utf-8").write(text)
