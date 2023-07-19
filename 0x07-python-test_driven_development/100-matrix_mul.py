#!/usr/bin/python3

"""
This is the 'matrix_mul' module.

It contains a function that multiplies 2 matrices.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the resulting matrix.

    Args:
        m_a (list of lists of int/float): The first matrix to be multiplied.
        m_b (list of lists of int/float): The second matrix to be multiplied.

    Returns:
        list of lists of int/float: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists.
        ValueError: If m_a or m_b is empty or not a rectangle.
        TypeError: If any element in m_a or m_b is not an int or float.
        ValueError: If m_a and m_b cannot be multiplied.
    """
    # Validate m_a and m_b
    for matrix in [m_a, m_b]:
        if not isinstance(matrix, list):
            raise TypeError("m_a must be a list or m_b must be a list")

        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

        if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
            raise ValueError("m_a can't be empty or m_b can't be empty")

        if not all(isinstance(num, (int, float)) for row in matrix for num in row):
            raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

        if len(set(len(row) for row in matrix)) > 1:
            raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Validate matrix dimensions for multiplication
    rows_a, cols_a = len(m_a), len(m_a[0])
    rows_b, cols_b = len(m_b), len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
