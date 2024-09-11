#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            upper_char = chr(ord(char) - 32)
            print("{}".format(upper_char), end="")
        else:
            print("{}".format(char), end="")
