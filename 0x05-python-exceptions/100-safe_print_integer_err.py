#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format("Unknown format code 'd' for object of type 'str'"))
        return False
    else:
        return True
