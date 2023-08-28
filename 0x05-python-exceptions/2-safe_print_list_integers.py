#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except TypeError as te:
            pass
        except ValueError as ve:
            pass
        except IndexError as ie:
            raise IndexError("list index out of range")
    print()
    return num
