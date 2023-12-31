#!/usr/bin/python3
"""defines a text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """insert text after each line
    """
    txt = ""
    with open(filename) as file:
        for line in file:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w"):
        open(filename, "w").write(txt)
