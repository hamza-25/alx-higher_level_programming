#!/usr/bin/python3
def print_last_digit(number):
    l_num = abs(number) % 10
    print("{}".format(l_num))
    return l_num
