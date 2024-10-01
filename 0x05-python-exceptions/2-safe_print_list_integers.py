#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
	some_num = 0
	for members in range(x):
		try:
			print("{:d}".format(my_list[members]), end='')
		
		except (ValueError, TypeError):
			pass
	print()
	return some_num
