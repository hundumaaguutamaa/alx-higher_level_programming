#!/usr/bin/python3
""" Define the function that write a file"""


def write_file(filename="", text=""):
	"""Write a string to a UTF-8 text file"""
	
	with open(filename, "w", encoding="utf-8") as h:
		return h.write(text)
