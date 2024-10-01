#!/usr/bin/python3
"""
This modue defines a class Square that defines a square
"""


class Square:
    """
    Class square that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initiates private instance attribrute size and position
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position of the square, ensuring it's a tuple of two +ve ints
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the square of the area

        Returns:
            int: The area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
