#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:  # Check if the dictionary is empty or None
        return None
    return max(a_dictionary, key=a_dictionary.get)