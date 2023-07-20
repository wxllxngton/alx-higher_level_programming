#!/usr/bin/python3
"""
This is the 'Student' module.
"""

class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list of strings, optional): Only attribute names contained in this list must be retrieved.

        Returns:
            dict: The dictionary representation with a simple data structure for JSON serialization.
        """
        if attrs is None:
            return self.__dict__

        serializable_attributes = {}
        for key in attrs:
            if key in self.__dict__ and isinstance(self.__dict__[key], (list, dict, str, int, bool)):
                serializable_attributes[key] = self.__dict__[key]

        return serializable_attributes
