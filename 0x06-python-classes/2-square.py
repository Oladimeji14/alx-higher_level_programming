#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, new_size=0):
        """Initialize a new Square.
        Args:
            new_size (int): The size of the new square.
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size
