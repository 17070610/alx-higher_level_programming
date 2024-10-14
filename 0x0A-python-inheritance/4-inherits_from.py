#!/usr/bin/python3
"""
Defines a function that checks a subclass of a class
"""


def inherits_from(obj, a_class):
    """
    Checks if obj inherits directly or indirectly from a_class
    """

    if issubclass(obj, a_class):
        return True
    return False
