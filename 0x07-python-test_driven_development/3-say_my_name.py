#!/usr/bin/python3

"""
This is the 'say_my_name' module.

It contains a function that prints My name is <first name> <last name>.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed.

    Returns:
        Nothing.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    message = "My name is {} {}"
    print(message.format(first_name, last_name))
