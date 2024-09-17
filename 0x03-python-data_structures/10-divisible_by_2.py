#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store True/False values
    result = []

    for i in my_list:
        if (i % 2) == 0:
            result.append(True)  # the number is divisible by 2
        else:
            result.append(False)  # if the number is not divisible by 2
    return result
