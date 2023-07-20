#!/usr/bin/python3
"""
This is the 'save_to_json_file' module.

It contains a function that writes an Object to a text file, using a JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): The Python data structure to be written to a text file.
        filename (str): The filename to be written on.

    Returns:
        None.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
