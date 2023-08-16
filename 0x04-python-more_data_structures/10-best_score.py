#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for first in a_dictionary:
        big = a_dictionary[first]
        break
    for key in a_dictionary:
        if a_dictionary[key] >= big:
            big = a_dictionary[key]
    return big
