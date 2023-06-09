#!/usr/bin/python3
"""
Module to add two numbers
"""


def add_integer(a, b=98):
    """ Define a function that adds two integer,float numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The addition of the two numbers.

    Raises:
        TypeError: If numbers not integer, float numbers.

    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or a float")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or a float")


    a = int(a)
    b = int(b)
    
    return (a + b)

