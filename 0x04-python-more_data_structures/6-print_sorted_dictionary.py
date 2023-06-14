#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for listed in sorted(a_dictionary.items()):
        
        print("{}: {}".format(listed[0], listed[1]))

