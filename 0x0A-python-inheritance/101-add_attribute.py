#!/usr/bin/python3

"""Write a function add_attribute"""


def add_attribute(obj, attrib, value):
    
    if not hasattr(obj, '__dict__'):
        """raise exception"""
        raise TypeError("can't add new attribute")
    setattr(obj, attrib, value)
