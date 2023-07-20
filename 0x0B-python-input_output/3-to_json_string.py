#!/usr/bin/python3
"""
This is the 'to_json_string' module.

It contains a function that returns the JSON representation of an object (string).
"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized.

    Returns:
        str: The JSON representation of an object.
    """
    return json.dumps(my_obj)
