#!/usr/bin/python3

"""
This module contains a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return '\n'.join(str(self.print_symbol) *
                         self.width for _ in range(self.height))

    def __repr__(self):
        """
        Returns string represantation that can be used to recreate the object
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when an instance of a rectangle is deleted
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles which is bigger or if equal

        Raises:
            TypeError: If either instances is not Rectangle type
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new rectangle with the height and width equal to size
        """
        return cls(size, size)
