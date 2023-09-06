#!/usr/bin/python3

"""
7-rectangle module

This module defines the Rectangle class with width, height, area, perimeter, __str__, __repr__, and __del__ methods.
"""

class Rectangle:
    """
    A class representing a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.
        Increases the count of instances.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
            rectangle_string += str(self.print_symbol) * self.__width
            rectangle_string += "\n"
        return rectangle_string

    def __repr__(self):
        """
        Return a string representation of the rectangle object.

        Returns:
            str: The string representation of the rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor for the Rectangle class.

        Prints a message when the object is deleted.
        Decreases the count of instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
