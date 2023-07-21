#!/usr/bin/python3
"""
This is the 'Rectangle' module.
"""
 
# Base = __import__('base').Base

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
