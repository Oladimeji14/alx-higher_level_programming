#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, new_width=0, new_height=0):
        """Initialize a new Rectangle.

        Args:
            new_width (int): The width of the new rectangle.
            new_height (int): The height of the new rectangle.
        """
        self.width = new_width
        self.height = new_height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError("width must be an integer")
        if new_value < 0:
            raise ValueError("width must be >= 0")
        self.__width = new_value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError("height must be an integer")
        if new_value < 0:
            raise ValueError("height must be >= 0")
        self.__height = new_value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
