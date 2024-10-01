#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
	updated_list = []
	for elements in range(list_length):
		try:
			div_result = my_list_1[elements] / my_list_2[elements]

		except TypeError:
			print("wrong type")
			div_result = 0

		except ZeroDivisionError:
			print("division by 0")
			div_result = 0	

		except IndexError:
			print("out of range")

		finally:
			updated_list.append(div_result)
	return updated_list
