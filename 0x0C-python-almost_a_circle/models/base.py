#!/usr/bin/python3
"""
This is the 'Base' module.
"""

class Base:
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initializes a Base instance with id.
        
        Args:
            id (int): The id of the Base instance.
        """
        if id is not None: 
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
					
