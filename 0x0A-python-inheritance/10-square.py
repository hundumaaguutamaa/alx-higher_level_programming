#!/usr/bin/python3

"""importing BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle

"""A class square that inherites from rectangle"""


class Square(Rectangle):
    """subclass of Rectangle"""

    def __init__(self, size):
        """Initializes private attribute size and validate """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):

        """Implement class area"""
        return self.__size ** 2
