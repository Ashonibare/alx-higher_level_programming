#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Find elements that are in either set_1 or set_2, but not in both
    return set_1 ^ set_2
