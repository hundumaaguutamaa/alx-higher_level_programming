#!/usr/bin/python3

def new_in_list(my_list, idx, element):
	list_c = len(my_list)
	if idx < 0 or idx >= list_c:
		return my_list
	else:
		newer_list = my_list.copy()
		newer_list[idx] = element
	return newer_list

