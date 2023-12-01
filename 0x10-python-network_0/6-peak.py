#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Returns a peak in a list of unsorted integers."""
    
    if not list_of_integers:
        return None

    size = len(list_of_integers)
    low, high = 0, size - 1

    while low <= high:
        mid = (low + high) // 2
        peak = list_of_integers[mid]

        if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
            return peak
        elif peak < list_of_integers[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1

    return None
