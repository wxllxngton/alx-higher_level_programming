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
        
    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation with a simple data structure for JSON serialization.
        """
        serializable_attributes = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serializable_attributes[key] = value

        return serializable_attributes
