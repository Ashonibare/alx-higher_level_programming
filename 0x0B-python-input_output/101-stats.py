#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys

# Initialize variables to store metrics
total_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

try:
    for line in sys.stdin:
        line_count += 1

        try:
            # Parse each line for the required fields
            parts = line.split()
            if len(parts) < 7:
                continue
            
            # Get the file size and add to total
            file_size = int(parts[-1])
            total_size += file_size

            # Get the status code and increment its count if it's one of the expected ones
            status_code = parts[-2]
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        except Exception:
            pass

        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # When CTRL + C is pressed, print the statistics before exiting
    print_stats()
    raise

# After the last input line, print the statistics one final time
print_stats()
