#!/usr/bin/python3

"""
8-rectangle
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with private attributes W and H.
        Validates the W and H as positive integers using integer_validator.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
