#!/usr/bin/python3
"""
This is the 'append_after' module.

It contains a function that inserts a line of text to a file, after each line containing a specific string.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str, optional): The name of the file to be modified (default is an empty string).
        search_string (str, optional): The specific string to search for in each line (default is an empty string).
        new_string (str, optional): The line of text to be inserted after each line containing the search string (default is an empty string).

    Returns:
        None.
    """
    with open(filename, mode='r') as file:
        lines = file.readlines()

    with open(filename, mode='w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
