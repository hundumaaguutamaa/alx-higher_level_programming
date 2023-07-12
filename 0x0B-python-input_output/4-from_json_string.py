#!/usr/bin/python3

"""Convert JSON string to python data structure."""

import json
"""Import json"""


def from_json_string(my_str):
    """
     A function that returns an object (Python data structure)
     represented by a JSON string.
    """
    return json.loads(my_str)
