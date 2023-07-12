#!/usr/bin/python3

"""Dctionary description."""


def class_to_json(obj):
    """
    A function that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    args:
       obj: is an instance of a class class_to_json.
        
    """

    return obj.__dict__
