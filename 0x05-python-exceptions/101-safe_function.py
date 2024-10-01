#!/usr/bin/python3
import sys


def safe_function(fct, *args):
	try:
		num_div = (fct, *args)
		return num_div

	except (ValueError, TypeError, ZeroDivisionError, IndexError):
		print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
		return None