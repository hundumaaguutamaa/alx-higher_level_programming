#!/usr/bin/python3
"""Function that writes an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Function to write an object to a text file using JSON representation"""

    with open(filename, "w") as h:
        json.dump(my_obj, h)
