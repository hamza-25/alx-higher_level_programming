#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    if idx >= length:
        return None
    for i in range(length):
        if i == idx:
            print("Element at index {:d} is {:d}".format(i, my_list[i]))
