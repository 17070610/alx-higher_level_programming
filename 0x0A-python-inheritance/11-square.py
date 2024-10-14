#!/usr/bin/python3
"""
Defines a square class thet inherits from Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
square class
"""


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return("[Square] " + str(self.__size) + "/" + str(self.__size))
