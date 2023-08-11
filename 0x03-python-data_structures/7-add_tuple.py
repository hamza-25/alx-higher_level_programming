#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    num = 0
    for i in tuple_a:
        if num == 0:
            a += tuple_a[0]
        elif num == 1:
            b += tuple_a[1]
        num += 1
    num = 0
    for i in tuple_b:
        if num == 0:
            a += tuple_b[0]
        elif num == 1:
            b += tuple_b[1]
        num += 1
    new_tup = (a, b)
    return new_tup
