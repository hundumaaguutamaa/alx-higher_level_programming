#!/usr/bin/python3
"""Square Class: defines a square."""

class Square:

    def __init__(self, size=0):
        """ Inistiantiate attributes"""
        self.size = size

    @property
    def size(self):
        """ get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size assignment"""

        if type(value) is not int:
            raise TypeError('size must be an integer')

        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Returns area of the square"""
        return (self.__size * self.__size)

    def __lt__(self, other):
        """  Comparisition used lessthan """
        return self.area() < other.area()

    def __le__(self, other):
        """ less than or equal comparision """
        return self.area() <= other.area()

    def __eq__(self, other):
        """ equals to comparison """
        return self.area() == other.area()

    def __ne__(self, other):
        """ not equal comparison """
        return self.area() != other.area()

    def __gt__(self, other):
        """ greater than comparision """
        return self.area() > other.area()

    def __ge__(self, other):
        """ greater than or equal comparision """

        return self.area() >= other.area()
