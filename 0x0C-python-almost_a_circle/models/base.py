#!/usr/bin/python3
"""
This is the 'Base' module.
"""

import json
import os

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
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dicts): The list of dictionaries to be returned as a JSON string representation.

        Returns:
            If list_dictionaries is None or empty, return the string: "[]" else, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
            
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list of objects): The list of objects whose JSON string representation will be written to a file.

        Returns:
            None.
        """
        filename = f"{cls.__name__}.json"
        data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])  # Convert objects to dictionaries
        with open(filename, 'w') as file:
            file.write(data)
            
    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): The string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string, or an empty list if json_string is None or empty, or if the JSON string is invalid.
        """
        if not json_string:
            return []
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return []
            
    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        
        Args:
            dictionary (dict): A dictionary containing attribute values for the instance.
            
        Returns:
            instance: The instance with all attributes set.
        """
        dummy_instance = cls(1, 1)  # Create a dummy instance with any initial width and height values
        dummy_instance.update(**dictionary)  # Use update with **kwargs to set the attributes from the dictionary
        return dummy_instance
    
    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        Returns:
            list: The list of instances.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)

        return [cls.create(**dictionary) for dictionary in list_dicts]
        
            

					
