#!/usr/bin/python3
"""A clas rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle inherited from  BaseGeometry
    """
    def __init__(self, width, height):

        super().integer_validator("width", width)
        self.__width = width
        
        super().integer_validator("height", height)
        self.__height = height
