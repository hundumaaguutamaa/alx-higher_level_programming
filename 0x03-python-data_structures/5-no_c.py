#!/usr/bin/python3

new_string = ""
index = 0
while index < len(my_string):
    if my_string[index] != 'c' and my_string[index] != 'C':
        new_string += my_string[index]
    index += 1
	return new_string

