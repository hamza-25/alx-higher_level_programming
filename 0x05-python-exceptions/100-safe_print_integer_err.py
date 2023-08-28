#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except TypeError as te:
        print(te)
        return False
    else:
        return True
