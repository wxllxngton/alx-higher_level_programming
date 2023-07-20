#!/usr/bin/python3
"""
This is the 'class_to_json' module.

It contains a function that returns the dictionary description 
with simple data structure (list, dictionary, string, integer and boolean) 
for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary description with a simple data structure for JSON serialization.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Object must be an instance of a Class")

    serializable_attributes = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value

    return serializable_attributes
