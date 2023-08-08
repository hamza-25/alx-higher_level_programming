#!/usr/bin/python3
for i in range(-122, -96):
    j = 2
    if (j % 2) == 0:
        i *= -1
        j += 1
    else:
        i *= -1
        i -= 32 
        j += 1
print("{}".format(chr(i)), end="")

