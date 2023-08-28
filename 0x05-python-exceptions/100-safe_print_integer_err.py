#!/usr/bin/python3
from sys import stderr
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        print("Exception:", e, file=stderr)
        return (False)
