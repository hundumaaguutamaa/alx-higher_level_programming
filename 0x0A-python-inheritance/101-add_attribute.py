#!/usr/bin/python3

""" Raise a TypeError exception, with the message 
can't add new attribute if the object can’t have new attribute.
"""

def add_attribute(obj, name, value):
	"""Add new attribute to an object."""
	if hasattr(obj, name):
		setattr(obj, name, value)
	else:
		raise TypeError("can't add new attribute")

