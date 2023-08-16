#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    list_len = len(my_list) - 1
    for i in range(len(my_list)):
        while list_len >= 0:
            if my_list[i] == my_list[list_len]:
                break
            list_len -= 1
        else:
            total += my_list[i] + 1
    return total
