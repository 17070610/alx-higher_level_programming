#!/usr/bin/python3
def uppercase(str):
    for i, char in enumerate(str):
        if ord(char) in range(97, 123):
            upper_char = chr(ord(char) - 32)
            print("{}".format(upper_char), end="" if i != len(str) - 1 else "\n")
        else:
            print("{}".format(char), end="" if i != len(str) - 1 else "\n")
