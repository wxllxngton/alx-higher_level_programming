#!/usr/bin/python3
"""
This is the 'load_from_json_file' module.

It contains a function that creates an Object from a “JSON file”.
"""

import json

def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): The filename of the JSON file to be read.

    Returns:
        object: The Python data structure created from the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        obj = json.load(file)

    return obj
