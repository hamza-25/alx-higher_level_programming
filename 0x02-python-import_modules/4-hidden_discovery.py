#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    length = len(dir(hidden_4))
    list_1 = dir(hidden_4)
    for i in range(length):
        if list_1[i][0] != '_':
            print("{}".format(list_1[i]))
