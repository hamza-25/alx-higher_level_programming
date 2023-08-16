#!/usr/bin/python3
def best_score(a_dictionary):
    if Not a_dictionary:
        return (None)
    big = max(a_dictionary, key=a_dictionary.get)
    return big
