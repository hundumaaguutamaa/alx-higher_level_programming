#!/usr/bin/python3

"""import Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

"""A class square that inherites from rectangle"""


class Square(Rectangle):
    """Subclass of Rectangle class"""
    def __init__(self, size):
        """initialize private attribute size and validate"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Print returned a square description"""
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))
