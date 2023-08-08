#!/usr/bin/python3
CAP = 2
for i in range(-122, -96):
    if (CAP % 2) == 0:
        i *= -1
        CAP += 1
    else:
        i *= -1
        i -= 32
        CAP += 1
    print("{}".format(chr(i)), end='')
