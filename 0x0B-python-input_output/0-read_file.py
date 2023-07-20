#!/usr/bin/python3
"""
This is the 'read_file' module.

It contains a function that reads a text file (UTF8) and prints it to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str, optional): The name of the file to be read (default is an empty string).

    Returns:
        None.
    """
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        print(data)
