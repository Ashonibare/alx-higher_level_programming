#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value  # Add or update the key with the new value
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
