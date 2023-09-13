#!/usr/bin/python3

"""Inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """A Function that inserts a line of text to a file"""
    
    with open(filename, "r") as h:
        text_to_file = h.readlines()

    with open(filename, "w") as hu:
        str = ""
        for line in text_to_file:
            str += line
            
            if search_string in line:
                str += new_str
                
        hu.write(str)
