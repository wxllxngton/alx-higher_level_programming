#!/usr/bin/python3

"""
101-add_attribute
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to the object if possible, else raises TypeError e.
    """
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
