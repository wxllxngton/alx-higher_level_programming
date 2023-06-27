#!/usr/bin/python3
class Square:
    """
    Represents a square shape with a given size and position.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position of the square's top-left corner.

    Methods:
        area(): Calculates and returns the area of the square.
        my_print(): Prints a visual representation of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a specified size and position.

        Args:
            size (int): The size of the square's sides (default is 0).
            position (tuple): The position of the square's top-left corner (default is (0, 0)).

        Raises:
            TypeError: If the provided size is not an integer or the position is not a tuple of 2 positive integers.
            ValueError: If the provided size is less than 0.
        """
        self.__size = 0
        self.__position = (0, 0)

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square's top-left corner.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position of the square's top-left corner.

        Raises:
            TypeError: If the provided position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square.

        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
