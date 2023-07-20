#!/usr/bin/python3
"""
This is the 'from_json_string' module.

It contains a function that returns an object (Python data structure) represented by a JSON string.
"""

import json

def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
