#!/usr/bin/python3

    """JSON representation"""

import json
    """Import JSON module"""


def to_json_string(my_obj):
    """
     A function that returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
