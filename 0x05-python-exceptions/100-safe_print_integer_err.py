#!/usr/bin/python3
from sys import exc_info, stderr
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return (False)
    else:
        return (True)
