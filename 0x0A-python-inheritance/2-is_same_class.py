#!/usr/bin/python3

"""
2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is an instance of the specified class; else False.
    """
    return type(obj) == a_class
