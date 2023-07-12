#!/usr/bin/python3

"""Write a class"""


class Student:
    """A class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the attributes of Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, 'my_attribute', None):
        """Retrieving a dictionary representation of a Student instance."""
        if my_attribute is None:
            return self.__dict__

        else:
            i = {}
            for my_attribute in my_attribute:
                if hasattr(self, attr):
                    i[my_attribute] = getattr(self, my_attribute)
            return i
