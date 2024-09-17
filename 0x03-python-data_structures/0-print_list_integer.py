#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))  # Using str.format() to print each integer instead of a regular print function
