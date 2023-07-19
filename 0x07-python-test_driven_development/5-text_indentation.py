#!/usr/bin/python3

"""
This is the 'text_indentation' module.

It contains a function that prints a text with 2 new lines after each of these characters: ., ? and :.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Returns:
        Nothing.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in text:
        print(character, end="")
        if character in ['.', '?', ':']:
            print("\n" * 2, end="")

    print()
