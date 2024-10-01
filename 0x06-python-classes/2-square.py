#!/usr/bin/python3
"""
This modue defines a class Square that defines a square
"""


class Square:
    """
    Class square that defines a square
    """

    def __init__(self, size=0):
        """
        Initiates private instance attribute size

        Args:
            size(int): Size of the square

        Raises:
            TypeError: When size is not an integer
            ValueError: When size is less than 0
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
