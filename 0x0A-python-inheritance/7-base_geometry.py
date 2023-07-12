#!/usr/bin/python3

"""
7-base_geometry
"""


class BaseGeometry:
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value if it is an integer and greater than 0.
        Raises TypeError or ValueError if the validation fails.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

    def area(self):
        """
        Calculates and returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle's dimensions.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


r = Rectangle(3, 5)

print(r)
print(r.area())
