#!/usr/bin/python3

"""importing Rectangle, 9-rectangle.py"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square ineriting Rectangle"""
    def __init__(self, size):
        """Initializing private attribute size and validating"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Return and print the square description"""
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))
