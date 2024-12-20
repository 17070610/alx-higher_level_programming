#!/usr/bin/python3
"""
Implementing a Geometry class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Implements a rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Area method implemented
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print
        """
        return ("[Rectangle] " + str(self.width) + "/" + str(self.height))
