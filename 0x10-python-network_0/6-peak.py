#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
     """Returns a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    l, h = 0, len(list_of_integers) - 1

    while l < h:
        m = (l + h) // 2

        if list_of_integers[m] < list_of_integers[m + 1]:
            
            l = m + 1
            
        else:
            h = m

    return list_of_integers[l]
