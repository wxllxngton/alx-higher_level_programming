#!/usr/bin/python3

"""
This is the 'add_integer' module.

It contains a function that adds 2 integers.
"""

def add_integer(a, b=98):
    """
    Add 2 integers or floats and return their sum as an integer.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
        int: The addition of a and b as an integer.
        
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)
    return a + b
