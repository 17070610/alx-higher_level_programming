#!/usr/bin/python3
"""
This module defines a class LockedClass
"""


class LockedClass:
    """
    Locked class that allows the user to only create no new instance except
    first class
    """
    __slots__ = ['first_name']
