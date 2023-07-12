#!/usr/bin/python3

"""
7-base_geometry
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    """
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
