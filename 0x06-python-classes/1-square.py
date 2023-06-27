#!/usr/bin/python3

"""
Module 1: Square
"""

class Square:
    """
    Represents a square shape.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square. Must be an integer.
        """
        self.__size = size
