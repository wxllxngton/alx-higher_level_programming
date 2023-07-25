#!/usr/bin/python3
"""
This is the 'Base' module.
"""

import json
import os
import csv

class Base:
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initializes a Base instance with id.
        
        Args:
            id (int): The id of the Base instance.
        """
        if id is not None: 
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        # ... (existing code)

    @classmethod
    def save_to_file(cls, list_objs):
        # ... (existing code)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to CSV format and writes it to a file.

        Args:
            list_objs (list of objects): The list of objects to be serialized.

        Returns:
            None.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == 'Rectangle':
                writer.writerow(['id', 'width', 'height', 'x', 'y'])
            elif cls.__name__ == 'Square':
                writer.writerow(['id', 'size', 'x', 'y'])
            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @staticmethod
    def from_json_string(json_string):
        # ... (existing code)

    @classmethod
    def create(cls, **dictionary):
        # ... (existing code)

    @classmethod
    def load_from_file(cls):
        # ... (existing code)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a list of objects from CSV format and returns a list of instances.

        Returns:
            list: The list of instances.
        """
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            list_dicts = [dict(row) for row in reader]

        return [cls.create(**dictionary) for dictionary in list_dicts]
