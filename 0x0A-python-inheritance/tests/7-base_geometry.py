#!/usr/bin/python3
"""
Defines a class BaseGeometry
"""


class BaseGeometry():
    """
    defines the area method
    """
    def area(self):
        """
        The public instance area
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
