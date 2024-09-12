#!/usr/bin/python3
import sys

# Get the number of arguments (excluding the script name)
num_args = len(sys.argv) - 1

# Determine if the output should use "argument" or "arguments"
arg_word = "argument" if num_args == 1 else "arguments"

# Prepare the list of arguments, joined by newlines
args_list = "\n".join(sys.argv[1:])

# Print the number of arguments and the arguments list in one print statement
print("{} {}{}".format(num_args, arg_word, f":\n{args_list}" if num_args > 0 else ""))
