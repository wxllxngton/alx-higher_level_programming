#!/usr/bin/python3
import math

class MagicClass:
    """
    Represents a magic circle with a given radius.

    Attributes:
        radius (float or int): The radius of the magic circle.

    Methods:
        area(): Calculates and returns the area of the magic circle.
        circumference(): Calculates and returns the circumference of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a specified radius.

        Args:
            radius (float or int): The radius of the magic circle (default is 0).

        Raises:
            TypeError: If the provided radius is not a number (float or int).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the magic circle.

        Returns:
            float or int: The area of the magic circle.
        """
        return math.pi * self.__radius**2

    def circumference(self):
        """
        Calculate and return the circumference of the magic circle.

        Returns:
            float or int: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius

