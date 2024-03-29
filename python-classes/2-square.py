#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """
    Square class: defines a square by a private instance attribute size.

    Attributes:
        __size (int): size of the square.

    """
    def __init__(self, size=0):
        """
        Initializes a square instance with an optional size.

        Args:
            size (int): size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
