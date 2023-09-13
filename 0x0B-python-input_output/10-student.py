#!/usr/bin/python3

"""A class Student"""


class Student:
    """Defining a class Student"""
    def __init__(self, first_name, last_name, age):
        """Initializing the attributes of class Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
		
        if attrs is None:
            return self.__dict__

        else:
            h = {}
            for attr in attrs:
                if hasattr(self, attr):
                    h[attr] = getattr(self, attr)
            return h
