#!/usr/bin/python3

"""
1-my_list
"""


class MyList(list):
    """
    Custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
