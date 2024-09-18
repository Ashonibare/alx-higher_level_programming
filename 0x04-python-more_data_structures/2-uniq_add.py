#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()  # Set to track unique integers
    total_sum = 0  # Initialize sum to 0

    # Loop through each integer in the list
    for number in my_list:
        #  check if int is not in set
        if number not in unique_integers:
            unique_integers.add(number)  # Add the integer to the set
            total_sum += number  # Add the integer to the total sum

    return total_sum  # Return the sum of unique integers
