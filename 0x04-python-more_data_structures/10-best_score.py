#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    for key, value in a_dictionary.items():
        if (value > best_score):
            best_score = value
        else:
            return None
    return best_score
