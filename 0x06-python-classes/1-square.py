#!/usr/bin/python3
class Square:
    """
    Square class represents a square shape.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square. Must be an integer.

        Raises:
            TypeError: If size is not an integer.
        """
        self.__size = size

