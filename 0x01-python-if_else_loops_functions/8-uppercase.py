#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 122):
            str[i] = chr(ord(str[i]) - 32)
        print("{}".format(c), end="")
    print("")
