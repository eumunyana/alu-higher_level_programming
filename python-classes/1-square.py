#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """
    Square class: defines a square by a private instance attribute size.

    Attributes:
        __size (int): size of the square.

    """
    def __init__(self, size):
        """
        Initializes a square instance.

        Args:
            size (int): size of the square.

        """
        self.__size = size
