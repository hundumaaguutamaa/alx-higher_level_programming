#!/usr/bin/python3

"""Used module 8-base_geometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Enherited form BaseGeometry class"""

    def __init__(self, width, height):
        """inistantiate attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
