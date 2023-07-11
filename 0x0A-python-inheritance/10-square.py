#!/usr/bin/python3

""" Import BaseGeometry and Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle
"""Write a class square that inherites from rectangle"""


class Square(Rectangle):
    """A subclass of Rectangle"""
    def __init__(self, size):
        """initialize private attribute size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return area of a square"""
        return self.__size ** 2
