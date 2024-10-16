#!/usr/bin/python3
"""
Contains a function that reads a text file and prints int to stdout
"""


def read_file(filename=""):
    """
    The read file function
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        for line in f:
            print(line, end="")
