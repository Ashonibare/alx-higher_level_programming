#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    some_num = 0
    try:
        for number in range(x):
            print("{}".format(my_list[number]), end='')
            some_num += 1
    except IndexError:
        pass
    print()
    return some_num
