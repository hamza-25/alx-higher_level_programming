#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    char = ""
    for i in sentence:
        length += 1
    if sentence[0] == " ":
        char = 'None'
    else:
        char = sentence[0]
    tup = (length, char)
    return (tup)
