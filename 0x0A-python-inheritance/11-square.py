#!/usr/bin/python3

"""
11-square
"""


class Sqaure(Rectangle):
    def __init__(self, width, height):
        """
        Initializes a Sqaure instance with private attributes W and H.
        Validates the W and H as positive integers using integer_validator.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the Sqaure.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Sqaure's dimensions.
        """
        return f"[Sqaure] {self.__width}/{self.__height}"
