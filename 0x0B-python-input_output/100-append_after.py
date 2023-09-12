#!/usr/bin/python3
"""defines a text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """insert text after each line 
    """
    txt = ""
    with open(filename) as f:
        for line in f:
            txt += line
            if search_str in line:
                txt += new_str
    with open(filename, "w"):
        open(filename, "w").write(text)
