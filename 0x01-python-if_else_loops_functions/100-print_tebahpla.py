#!/usr/bin/python3
CAP = 2

for i in range(-122, -96):
    temp = i
    if (CAP % 2) == 0:
        temp *= -1
        CAP += 1
    else:
        temp *= -1
        temp -= 32
        CAP += 1
    print("{}".format(chr(i)), end='')
