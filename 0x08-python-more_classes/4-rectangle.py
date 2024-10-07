#!/usr/bin/python3

"""
This module contains a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width of the rectangle

        Raises:
            TypeError: When value is not an integer
            ValueError: When value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the recatangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height of the rectangle

        Raises:
            TypeError: When the value is not an integer
            ValueError: When the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        perimeter = 2 * (self.__width + self.__height)
        if (self.__width == 0 or self.__height == 0):
            perimeter = 0

        return perimeter

    def __str__(self):
        """
        Prints the rectangle with character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join('#' * self.width for _ in range(self.height))

    def __repr__(self):
        """
        Returns string represantation that can be used to recreate the object
        """

        return "Rectangle({}, {})".format(self.width, self.height)
