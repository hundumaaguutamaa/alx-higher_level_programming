#!/usr/bin/python3

""" Write the first class Base: """

import json
import os
import csv
import turtle


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writing JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_str = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(json_str)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return list of the JSON string representation json_string:"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set:"""
        if cls.__name__ == "Square":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ Add class method and return a list of instances."""
        filename = cls.__name__ + '.json'
        if not os.path.exists(filename):
            return []
        
        with open(filename, 'r') as file:
            list_dicts = cls.from_json_string(file.read())
        
        return [cls.create(**dict_obj) for dict_obj in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves list objects to CSV file."""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is not None and len(list_objs) > 0:
                writer = csv.writer(csvfile)
                writer.writerow(list_objs[0].to_dictionary().keys())
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Reads CSV file datas."""
        filename = cls.__name__ + '.csv'
        if not os.path.exists(filename):
            return []
        
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            list_dicts = [dict(zip(headers, row)) for row in reader]
        
        return [cls.create(**dict_obj) for dict_obj in list_dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares:"""
