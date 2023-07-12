#!/usr/bin/python3

"""Appending text to end of a file."""


def append_write(filename="", text=""):
    """
    Append a string to the end,
    and returns the number of characters added.
    """
    with open(filename, 'a') as f:
        return f.write(text)
