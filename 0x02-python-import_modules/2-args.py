#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length == 0:
        print("{} arguments.".format(0))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, sys.argv[length]))
    else:
        print("{} arguments:".format(length))
        counter = 1
        for i in range(length):
            print("{}: {}".format(counter, sys.argv[i + 1]))
            counter += 1
