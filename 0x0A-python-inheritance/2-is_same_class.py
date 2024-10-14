#!/usr/bin/python3
"""
Defines a class-checking function
"""


def is_same_class(obj, a_class):
    """
    It checks if obj is an instance of a_class
    """
    if type(obj) == a_class:
        return True
    return False
