#!/usr/bin/python3
"""
This is the 'Base' module.
"""

import json

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
            
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dicts): The list of dictionaries to be returned as a JSON string representation.

        Returns:
            If list_dictionaries is None or empty, return the string: "[]" else, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
            
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list of objects): The list of objects whose JSON string representation will be written to a file.

        Returns:
            None.
        """
        filename = f"{cls.__name__}.json"
        data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])  # Convert objects to dictionaries
        with open(filename, 'w') as file:
            file.write(data)
            
    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): The string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string, or an empty list if json_string is None or empty, or if the JSON string is invalid.
        """
        if not json_string:
            return []
        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return []
        
            


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle with width, height, x, y, id.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x position of the rectangle.
            y (int, optional): The y position of the rectangle.
            id (int, optional): The id of the Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x position of the rectangle.

        Args:
            value (int): The x value to set.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y position of the rectangle.

        Args:
            value (int): The y value to set.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """
        Computes and returns the area of the rectangle.
        
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height
        
    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #.
        
        Returns:
            None.
        """
        for y_offset in range(self.__y):
            print()
        for height in range(self.__height):
            for x_offset in range(self.__x):
                print(" ", end="")
            for width in range(self.__width):
                print("#", end="")
            print()
                
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
        
        
    def update(self, *args, **kwargs):
        """
        Assigns arguments to each attribute in the order: id, width, height, x, y.
    
        Args:
            *args: Variable number of no-keyword arguments representing id, width, height, x, y.
            **kwargs: Variable number of keyworded arguments representing id, width, height, x, y.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']
                
    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
            dict: The dictionary representation of a Rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
                
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

        
if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))
