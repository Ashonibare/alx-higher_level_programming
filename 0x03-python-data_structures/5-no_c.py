#!/usr/bin/python3
def no_c(my_string):
    # Use string translation to remove 'c' and 'C'
    return my_string.translate(str.maketrans('', '', 'cC'))
