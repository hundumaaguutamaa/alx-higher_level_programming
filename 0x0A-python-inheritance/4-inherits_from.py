#!/usr/bin/python3

"""Used module 4-inherits_from"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    """
    return not isinstance(obj, a_class) and type(obj) != a_class
