#!/usr/bin/python3
"""Defines reading function"""


def read_file(filename=""):
    """print read file"""
    with open(filename, encoding="utf-8"):
        print(open(filename, encoding="utf-8").read(), end="")
