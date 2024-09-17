#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # if the list is empty
        return None  # Return None

    largest_number = my_list[0]  # Assumes element 1 is the largest

    for number in my_list:
        if number > largest_number:
            largest_number = number

    return largest_number
