#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0, 
                "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            status_code = tokens[-2]
            file_size_token = tokens[-1]

            if status_code in status_tally:
                status_tally[status_code] += 1

            try:
                file_size += int(file_size_token)
            except ValueError:
                continue

        line_count += 1

        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print("File size: {}".format(file_size))
            for code, count in sorted(status_tally.items()):
                if count:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    # Print the statistics on Keyboard Interrupt (CTRL + C)
    print("File size: {}".format(file_size))
    for code, count in sorted(status_tally.items()):
        if count:
            print("{}: {}".format(code, count))

# Print the statistics after the loop finishes
print("File size: {}".format(file_size))
for code, count in sorted(status_tally.items()):
    if count:
        print("{}: {}".format(code, count))
