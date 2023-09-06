#!/usr/bin/python3
"""matrix function"""


def matrix_divided(matrix, div):
    """
    function that devide matrix item

    Args:
        @matrix: matrix that contain item
        @div: number to div
    Return:
        return new matrix divide by div param

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, int) for row in matrix for ele in row)):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    row_len = []
    for row in matrix:
        if len(row) in row_len:
            continue
        row_len.append(len(row))
    if len(row_len) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrix
