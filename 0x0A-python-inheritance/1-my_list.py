#!/usr/bin/python3

class MyList(list):
    """ Class that inherits class list.

    Args:
        list: a class list

    """

    def print_sorted(self):
        """ A method to print the sorted list """
        list_sorted = self.copy()
        list_sorted.sort()
        print(list_sorted)
