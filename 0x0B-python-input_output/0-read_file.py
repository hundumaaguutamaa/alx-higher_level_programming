#!/usr/bin/python3

"""Function to read from a file"""


def read_file(filename=""):
    """Reads a text from file and prints"""
    with open(filename) as f:
        reaad_file = f.read()
    print(reaad_file, end="")
