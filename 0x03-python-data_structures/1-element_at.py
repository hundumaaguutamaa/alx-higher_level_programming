#!/usr/bin/python3

def element_at(my_list, idx):
    counter = len(my_list)

    if idx < 0 or idx >= counter:
        return None
    else:
        return my_list[idx]

