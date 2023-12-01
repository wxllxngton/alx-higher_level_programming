#!/usr/bin/python3
"""
Script to find a peak in a list of integers for interview preparation.
"""

"""
    THOUGHT PROCESS
        Since the list is not sorted, sorting would take O(n*log(n)).
            -> Not worth sorting.
        Looping through and keeping track of the maximum (brute force).
            -> O(n)
        Possibly looping from each end and reducing to 1/2 run time.
            -> Still O(n)
"""


def find_peak(list_of_integers):
    """Find and return the peak element in the given list of integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int or None: The peak element if found, None if the list is empty.
    """
    peak_element = None
    for element in list_of_integers:
        if peak_element is None or peak_element < element:
            peak_element = element
    return peak_element
