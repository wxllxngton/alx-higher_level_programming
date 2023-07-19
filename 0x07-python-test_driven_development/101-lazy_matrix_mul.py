#!/usr/bin/python3

"""
This is the 'lazy_matrix_mul' module.

It contains a function that multiplies 2 matrices by using the module NumPy.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the resulting matrix.

    Args:
        m_a (list of lists of int/float): The first matrix to be multiplied.
        m_b (list of lists of int/float): The second matrix to be multiplied.

    Returns:
        list of lists of int/float: The resulting matrix after multiplication.

    Raises:
        ValueError: If m_a or m_b is not a valid matrix for multiplication.
    """
    try:
        result = np.dot(m_a, m_b)
        return result.tolist()
    except Exception as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
