#!/usr/bin/python3

""" Write the first class Base: """

class Base:
    """The private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base instance/constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Defining static method that returns json string representation."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
