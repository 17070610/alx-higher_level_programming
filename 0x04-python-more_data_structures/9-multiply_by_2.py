#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary:
        a_dictionary[key] = a_dictionary[key] * 2
        new_dictionary.append(a_dictionary[key])
    return new_dctionary
