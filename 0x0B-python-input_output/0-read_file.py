#!/usr/bin/python3
"""A function that reads UTF8 file and prints to stdout"""


def write_file(filename=""):
    """Read file and prints to stdout"""
    with open(filename, encoding="utf-8") as h:
        """ Opening the file with encoding utf-8"""
        print(h.read(), end="")
