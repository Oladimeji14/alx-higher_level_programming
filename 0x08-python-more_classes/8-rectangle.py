#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        rect_instances (int): The number of Rectangle instances.
        print_sym (any): The symbol used for string representation.
    """

    rect_instances = 0
    print_sym = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).rect_instances += 1
        self.wid = width
        self.hei = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.wid

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.wid = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.hei

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.hei = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.wid * self.hei)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.wid == 0 or self.hei == 0:
            return (0)
        return ((self.wid * 2) + (self.hei * 2))

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        """Return the Rectangle with the greater area.

        Args:
            rect1 (Rectangle): The first Rectangle.
            rect2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect1 or rect2 is not a Rectangle.
        """
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect2 must be an instance of Rectangle")
        if rect1.area() >= rect2.area():
            return (rect1)
        return (rect2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.wid == 0 or self.hei == 0:
            return ("")

        rect = []
        for i in range(self.hei):
            [rect.append(str(self.print_sym)) for j in range(self.wid)]
            if i != self.hei - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.wid)
        rect += ", " + str(self.hei) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).rect_instances -= 1
        print("Bye rectangle...")