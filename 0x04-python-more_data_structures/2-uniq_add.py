#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    uniq = [i for i in my_list if my_list.count(i) == 1]
    for j in uniq:
        total += j + 1
    return total
