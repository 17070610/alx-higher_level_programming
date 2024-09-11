#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            upper_char = chr(ord(char) - 32)
            print("{}".format(upper_char), end="" if char != len(str) - 1 else "\n")
        else:
            print("{}".format(char), end="" if char != len(str) - 1 else "\n")
