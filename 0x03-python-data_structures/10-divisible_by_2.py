#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    index = 0
    for i in my_list:
        if (i % 2) == 0:
            new_list[index] = True
        else:
            new_list[index] = False
        index += 1
    return (new_list)
