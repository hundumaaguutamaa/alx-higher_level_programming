#!/usr/bin/python3

"""A class student"""


class Student:
    """Defines a class Student."""
    def __init__(self, first_name, last_name, age):
        """Initialize attributes of Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, 'my_attribute', None):
        """Retrieve a dictionary representation of a Student instance."""
        if my_attribute is None:
            return self.__dict__

        else:
            i = {}
            for my_attribute in my_attribute:
                if hasattr(self, my_attribute):
                    i[my_attribute] = getattr(self, my_attribute)
            return i

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for keys in json:
            setattr(self, keys, json[keys])
