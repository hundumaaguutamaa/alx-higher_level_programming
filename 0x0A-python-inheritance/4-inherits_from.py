#!/usr/bin/python3

"""module for a class"""


def inherits_from(obj, a_class):
    """check for subclass inheritance"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
