#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return None
    for i in range(length):
        if i == idx:
            print("Element at index {} is {}".format(i, my_list[i]))
