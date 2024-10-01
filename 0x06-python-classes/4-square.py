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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            self.__size(int): Size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter to set the value of the size of the square

        Raises:
            TypeError: When value isn't an integer
            ValueError: When value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the square of the area

        Returns:
            int: The area of a square
        """
        return self.__size ** 2
