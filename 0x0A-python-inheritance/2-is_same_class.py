#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ Function that returns True/False checking if obj is a type of a_class.

    Args:
        obj: object
        a_class: class type

    Returns:
        True, if type of obj is of a_class or,
        False
    """
    return type(obj) is a_class

