#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    # Initialize the sum to 0
    total_sum = 0

    # Loop through all arguments starting from index 1 (skipping the script name)
    for arg in sys.argv[1:]:
        try:
            # Convert each argument to an integer and add to the sum
            total_sum += int(arg)
        except ValueError:
            # Ignore non-numeric arguments
            pass

    # Print the total sum of all numeric arguments
    print(total_sum)
