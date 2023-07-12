# Functions and Classes

This repository contains the following functions and classes:

## 0-lookup.py

### `lookup(obj)`

Returns a list of available attributes and methods of an object.

---

## 2-is_same_class.py

### `is_same_class(obj, a_class)`

Returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

---

## 3-is_kind_of_class.py

### `is_kind_of_class(obj, a_class)`

Returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

---

## 4-inherits_from.py

### `inherits_from(obj, a_class)`

Returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

---

## 7-base_geometry.py

### `BaseGeometry`

A base class for geometry-related operations.

#### Public Methods

- `area()`: Raises an Exception with the message 'area() is not implemented'.
- `integer_validator(name, value)`: Validates the value if it is an integer and greater than 0. Raises TypeError or ValueError if the validation fails.

---

## 9-rectangle.py

### `Rectangle`

A class that represents a rectangle and inherits from `BaseGeometry`.

#### Public Methods

- `__init__(self, width, height)`: Initializes a Rectangle instance with private attributes `width` and `height`. Validates the width and height as positive integers using `integer_validator`.
- `area()`: Calculates and returns the area of the Rectangle.
- `__str__()`: Returns a string representation of the Rectangle in the format '[Rectangle] <width>/<height>'.

---

## 11-square.py

### `Square`

A class that represents a square and inherits from `Rectangle`.

#### Public Methods

- `__init__(self, size)`: Initializes a Square instance with private attribute `size`. Validates the size as a positive integer using `integer_validator`.
- `area()`: Calculates and returns the area of the Square.

---

## 100-my_int.py

### `MyInt`

A class that represents a rebellious integer and inherits from `int`.

#### Custom Operators

- `==` and `!=`: The equality and inequality operators are inverted.

---

## 101-add_attribute.py

### `add_new_attribute(obj, attribute, value)`

Adds a new attribute to the object if possible, or raises a TypeError exception with the message "can't add new attribute" if the object can't have a new attribute.

