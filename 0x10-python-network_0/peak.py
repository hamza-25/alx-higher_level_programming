#!/usr/bin/python3
def find_peak(list_of_integers):
    length = len(list_of_integers)

    if length == 0:
        return None

    if length == 1:
        return list_of_integers[0]

    for i in range(1, length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

    # Check the first and last elements separately
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    return None  # No peak found

# Example usage:
my_list = [1, 3, 20, 4, 1, 0]
result = find_peak(my_list)
print(result)

