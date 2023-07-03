#!/usr/bin/python3
class Rectangle:
	number_of_instances = 0
	print_symbol = "#"

	def __init__(self, width=0, height=0):
		self.__height = height
		self.__width = width
		Rectangle.number_of_instances += 1

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		elif value < 0:
			raise ValueError("height must be >= 0")
		else:
			self.__height = value

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		elif value < 0:
			raise ValueError("width must be >= 0")
		else:
			self.__width = value

	def area(self):
		return self.__width * self.__height

	def perimeter(self):
		if self.__width == 0 or self.__height == 0:
			return 0
		return (self.__width * 2) + (self.__height * 2)

	def __str__(self):
		rectangle_string = ""
		if self.__width == 0 or self.__height == 0:
			return rectangle_string
		for _ in range(self.__height):
			rectangle_string += str(self.print_symbol) * self.__width
			rectangle_string += "\n"
		return rectangle_string

	def __repr__(self):
		return f"Rectangle({self.__width}, {self.__height})"

	def __del__(self):
		print("Bye rectangle...")
		Rectangle.number_of_instances -= 1

	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		if not isinstance(rect_1, Rectangle):
			raise TypeError("rect_1 must be an instance of Rectangle")
		elif not isinstance(rect_2, Rectangle):
			raise TypeError("rect_2 must be an instance of Rectangle")
		elif rect_1.area() >= rect_2.area():
			return rect_1
		else:
			return rect_2

	@classmethod
	def square(cls, size=0):
		return cls(size, size)
