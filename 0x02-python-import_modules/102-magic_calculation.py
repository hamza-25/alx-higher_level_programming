#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import sub, add
    if a > b:
        return sub(a, b)
    else:
        sum = add(a, b)
        for j in range(4, 6):
            sum = add(sum, j)
        return sum
