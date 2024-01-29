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
        return self.__new_width

    @width.setter
    def width(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError("width must be an integer")
        if new_value < 0:
            raise ValueError("width must be >= 0")
        self.__new_width = new_value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__new_height

    @height.setter
    def height(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError("height must be an integer")
        if new_value < 0:
            raise ValueError("height must be >= 0")
        self.__new_height = new_value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__new_width * self.__new_height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__new_width == 0 or self.__new_height == 0:
            return (0)
        return ((self.__new_width * 2) + (self.__new_height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__new_width == 0 or self.__new_height == 0:
            return ("")

        new_rect = []
        for i in range(self.__new_height):
            [new_rect.append('#') for j in range(self.__new_width)]
            if i != self.__new_height - 1:
                new_rect.append("\n")
        return ("".join(new_rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        new_rect = "Rectangle(" + str(self.__new_width)
        new_rect += ", " + str(self.__new_height) + ")"
        return (new_rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
