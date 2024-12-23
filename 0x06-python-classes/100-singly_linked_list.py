#!/usr/bin/python3
"""
This module contains a class Node that defines a node of a singly linked list
"""


class Node:
    """
    This class defines a node of a singly linked list

    Attributes:
        data(int): The integer containing data of the current node
        next_node: The next node of the list
    """

    self.__data = data
    self.__next_node = next_node

    @property
    def data(self):
        """
        This method retrieves the attribute data
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        This method sets the value of the data attribute

        Raises:
                TypeError: if an value not an integer
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        This method retrieves the attribute next_node
        """

        return self.__next

    @next_node.setter
    def next_node(self, value):
        """
        This method sets the value of the next_node

        Raises:
            TypeError: if the value is not either none or a Node object
        """

        
