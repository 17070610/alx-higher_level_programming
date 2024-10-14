#!/usr/bin/python3
"""
A functions checks if a class and inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is inherited from a_class
    """

    if isinstance(obj, a_class):
        return True
    return False
