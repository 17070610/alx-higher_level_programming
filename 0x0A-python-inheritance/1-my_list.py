#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """
    This is class MyList that defines print_sorted method
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
