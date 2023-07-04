#!/usr/bin/python3

"""
LockedClass Module
"""

class LockedClass:
    """A class that prevents dynamic creation of instance attributes, except for 'first_name'."""

    # Limit the allowed instance attributes to 'first_name' using __slots__
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """
        Override the attribute assignment behavior.

        Args:
            name (str): The name of the attribute being assigned.
            value: The value to be assigned to the attribute.

        Raises:
            AttributeError: If the attribute being assigned is not 'first_name'.

        Note:
            This method is called whenever an attribute assignment is attempted.
            It allows assignment of 'first_name' instance attribute and raises
            an AttributeError for any other attribute assignment.
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object does not support attribute assignment")
        self.__dict__[name] = value
