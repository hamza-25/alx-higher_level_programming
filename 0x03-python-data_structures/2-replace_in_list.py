#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return None
    for i in range(length):
        if i == idx:
            my_list[i] = element
