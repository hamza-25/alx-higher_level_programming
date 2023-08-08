#!/usr/bin/python3
def mult_three(num):
    for i in range(1, 101):
        if num == (i * 3):
            return True
    return False


def mult_five(num):
    for i in range(1, 101):
        if num == (i * 5):
            return True
    return False


def fizzbuzz():
    for i in range(1, 101):
        if mult_three(i) and mult_five(i):
            print("FizzBuzz", end=" ")
        elif mult_three(i):
            print("Fizz", end=" ")
        elif mult_five(i):
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
