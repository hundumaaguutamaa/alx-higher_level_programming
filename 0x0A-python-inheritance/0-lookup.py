#!/usr/bin/python3
"""Returns a list of all available attributes and methods."""


def lookup(obj):
	"""Returns list of attributes and methods of obj."""
    return dir(obj)
