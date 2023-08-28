#!/usr/bin/python3
from sys import exc_info, stderr
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError)as e:
        print("Exception:", e, file=stderr)
        return (False)
    else:
        return (True)
