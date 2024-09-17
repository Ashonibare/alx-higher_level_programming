#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is out of range
    if idx < 0 or idx >= len(my_list):
        return my_list  # If out of range, return the original list
    else:
        del my_list[idx]  # Delete the item at the given index
    return my_list  # Return the modified list after deletion
