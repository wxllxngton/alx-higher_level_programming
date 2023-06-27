#!/usr/bin/python3

"""
Module: 103
"""

class Square:
    """
    Represents a square shape with a given size.

    Attributes:
        size (float or int): The size of the square.

    Methods:
        area(): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square instance with a specified size.

        Args:
            size (float or int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If the provided size is not a number (float or int).
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two Square instances for equality based on their areas.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compare two Square instances for inequality based on their areas.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compare two Square instances to check if the area of the current Square is greater.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool or NotImplemented: True if the current square's area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Compare two Square instances to check if the area of the current Square is greater or equal.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool or NotImplemented: True if the current square's area is greater or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Compare two Square instances to check if the area of the current Square is smaller.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool or NotImplemented: True if the current square's area is smaller, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Compare two Square instances to check if the area of the current Square is smaller or equal.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool or NotImplemented: True if the current square's area is smaller or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
