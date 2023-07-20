#!/usr/bin/python3
"""
This is the 'write_file' module.

It contains a function that writes a string to a text file (UTF8) and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str, optional): The name of the file to be written on (default is an empty string).
        text (str, optional): The text to be written on the file (default is an empty string).

    Returns:
        int: The number of characters written.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
