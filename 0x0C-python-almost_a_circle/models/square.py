#!/usr/bin/python3
"""
This is the 'Square' module.
"""

Rectangle = __import__('rectangle').Rectangle
                
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square instance with size, x, y and id.
        
        Args:
            size (int): The size of the square.
            x (int, optional): The x position of the square.
            y (int, optional): The y position of the square.
            id (int, optional): The id of the square instance.
        """
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to set.
        """
        self.width = value
        self.height = value
        
    def update(self, *args, **kwargs):
        """
        Assigns arguments to each attribute in the order: id, size, x, y.
    
        Args:
            *args: Variable number of no-keyword arguments representing id, size, x, y.
            **kwargs: Variable number of keyworded arguments representing id, size, x, y.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']
                
    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.

        Returns:
            dict: The dictionary representation of a Square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
                
        
    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A formatted string representing the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

        
