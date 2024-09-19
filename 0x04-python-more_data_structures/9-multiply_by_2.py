#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {k: v * 2 for k, v in a_dictionary.items()}


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
