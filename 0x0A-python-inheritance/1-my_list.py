#!/usr/bin/python3
"""
This module defines a class MyList that is a subclass of list
"""


class MyList(list):
    """
    This is class MyList that defines print_sorted method
    """
    def __init__(self):
        """
        Initializes the object
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
