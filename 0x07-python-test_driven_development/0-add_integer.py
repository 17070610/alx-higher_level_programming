#!/usr/bin/python3
"""
Defines an integer addition function
"""


def add_integer(a, b=98):
    """
    Returns the integer sum of a and b

    Float arguments are turned into ints before adding them

    Raises:
        TypeError: If a or b is neither int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
