#!/usr/bin/python3

"""
This is the 'add_items' script.

It adds all arguments to a Python list, and then saves them to a file.
"""

import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    """
    Main function to add arguments to a list and save them to a file.
    """
    args_items = [arg for arg in sys.argv[1:]]  # Ignore the first argument (script name)

    filename = "add_item.json"
    if exists(filename):
        existing_items = load_from_json_file(filename)
        args_items = existing_items + args_items

    save_to_json_file(args_items, filename)

if __name__ == "__main__":
    main()
