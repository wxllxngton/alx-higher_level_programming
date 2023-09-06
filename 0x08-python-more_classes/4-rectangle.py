#!/usr/bin/python3

"""
4-rectangle module

This module defines the Rectangle class with width, height, area, perimeter, __str__, and __repr__ methods.
"""

class Rectangle:
    """
    A class representing a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The calculated area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The calculated perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The rectangle string.
        """
        rectangle_string = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_string
        for _ in range(self.__height):
            rectangle_string += "#" * self.__width
            rectangle_string += "\n"
        return rectangle_string

    def __repr__(self):
        """
        Return a string representation of the rectangle object.

        Returns:
            str: The string representation of the rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"
