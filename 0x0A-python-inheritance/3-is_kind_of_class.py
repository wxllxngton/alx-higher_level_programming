#!/usr/bin/python3

"""
3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instanceof or inherited from a_class; else False.
    """
    return isinstance(obj, a_class)
