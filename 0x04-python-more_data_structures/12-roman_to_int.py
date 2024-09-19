#!/usr/bin/python3
def roman_to_int(roman_string):
    # Dictionary to store the Roman numerals and their int values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # If input is not a string or is None, return 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    total = 0
    prev_value = 0

    # Loop through the roman_string in reverse order
    for char in reversed(roman_string):
        value = roman_values.get(char, 0)

        # If current value is less than the previous one, subtract
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value  # Update previous value for the next iteration

    return total
