#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    # Retrieve the number of arguments (excluding the script name)
    num_args = len(sys.argv) - 1
    
    # Determine the correct wording for "argument" or "arguments"
    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))
        
        # Print each argument with its position
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
