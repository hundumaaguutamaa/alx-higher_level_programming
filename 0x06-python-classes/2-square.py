#!/usr/bin/python3

""" defines class named Square """

class Square:
    """ A class square defines a function named __init__ """
    def __init__(self, size=0):
        """ if statement check thee size """
        if type(size) != int:
            """ raise an exception error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise value error """
            raise ValueError("size must be >= 0")
        else:
            """ initializes __size of self which is size """
            self.__size = size
