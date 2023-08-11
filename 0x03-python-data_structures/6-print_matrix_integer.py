#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        length = len(i)
        itr = 1
        for j in i:
            if itr == length:
                print("{}$".format(j), end="")
                itr += 1
            else:
                print("{}".format(j), end=" ")
                itr += 1
        print("\n")
    else:
        print("--$")
