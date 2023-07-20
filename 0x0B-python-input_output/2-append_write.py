#!/usr/bin/python3
"""
This is the 'append_write' module.

It contains a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str, optional): The name of the file to be written on (default is an empty string).
        text (str, optional): The text to be written on the file (default is an empty string).

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a+", encoding="utf-8") as file:
        chars_added = file.write(text)

    return chars_added
