#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_scorer = None
    highest_score = float('-inf')

    for key, value in a_dictionary.items():
        if value > highest_score:
            best_scorer = key
    return best_scorer
