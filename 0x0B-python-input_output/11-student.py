#!/usr/bin/python3

"""Write a class student"""


class Student:
    """Defining class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializing the attributes of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        else:
            h = {}
            for attr in attrs:
                if hasattr(self, attr):
                    h[attr] = getattr(self, attr)
            return h

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instances"""
        for dict_keys in json:
            setattr(self, dict_keys, json[dict_keys])
