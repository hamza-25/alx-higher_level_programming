#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    int_list = []
    for c in roman_string:
        if c in roman_int:
            int_list.append(roman_int[c])
    total = 0
    for i in range(len(int_list)):
        if i == 0:
            total += int_list[i]
        elif int_list[i] <= int_list[i - 1]:
            total += int_list[i]
        else:
            total += int_list[i] - (int_list[i - 1] * 2)
    return total
