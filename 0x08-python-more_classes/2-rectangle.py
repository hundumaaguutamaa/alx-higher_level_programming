#!/usr/bin/python3


class Rectangle:
    """Defined a class Rectangle"""

    def __init__(self, width=0, height=0):
       """Initializes a rectangle method with attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
     """Returns a width method"""
        return self.__width

    @width.setter

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
      """Returns a height method"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns a area method"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns a perimeter method"""
        if self.__width == 0 or self.__height == 0:
            return (0)
            """Returns perimeter of rectangle"""
        return ((self.__width * 2) + (self.__height * 2))
