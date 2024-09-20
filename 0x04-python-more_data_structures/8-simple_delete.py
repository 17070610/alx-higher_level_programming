#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for init_key in a_dictionary:
        if init_key != key:
            return a_dictionary
        elif init_key == key:
            del a_dictionary[init_key]
    return a_dictionary
