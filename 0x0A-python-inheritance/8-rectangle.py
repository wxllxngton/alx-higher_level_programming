#!/usr/bin/python3

"""
8-rectangle
"""


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle and inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with private attributes width and height.
        Validates the width and height as positive integers using integer_validator.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
