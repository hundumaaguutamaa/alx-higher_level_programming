#!/usr/bin/python3
"""creates class Square which have
private instance, attribute size and public instance method"""


class Square:
    """defined class with instantiated, validated private instance attribute
and public instance method."""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculates and returns current square of the area"""
        
        return(self.__size * self.__size)

