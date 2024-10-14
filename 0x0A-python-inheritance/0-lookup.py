#!/usr/bin/python3
"""
This module returns the list of all available attributes and method of an obj
"""


def lookup(obj):
    """
    The function that returns available methods and attributes of an object
    """
    return dir(obj)
