#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    new = ""
    for i in range(len(str)):
        if i == n:
            continue
        new[count] = str[i]
        count += 1
