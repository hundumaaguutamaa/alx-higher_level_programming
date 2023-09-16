#!/usr/bin/python3
""" Function to add two integers."""


def add_integer(a, b=98):
    """Checkong data-type of variables."""
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
