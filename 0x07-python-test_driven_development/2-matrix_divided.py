#!/usr/bin/python3

"""
This is the 'matrix_divided' module.

It contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and return the new matrix.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int or float): The number to divide each element of the matrix by.

    Returns:
        list of lists of float: The new matrix with elements divided by 'div'.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If 'div' is not a number (integer or float).
        ZeroDivisionError: If 'div' is equal to 0.
    """
    # Check if the matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if 'div' is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if 'div' is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
