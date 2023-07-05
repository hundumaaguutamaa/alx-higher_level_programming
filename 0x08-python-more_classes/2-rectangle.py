#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Defined a class Rectangle"""

    def __init__(self, width=0, height=0):
       """Initializes a rectangle method with attributes
	args: 
	width:- width of the rectangle.
	height:- height of the rectangle.
	""""

        self.width = width
        self.height = height

    @property
    def width(self):
     """Set a width of the Rectangle"""
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
      """Set a height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns a perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
            """Returns perimeter of rectangle"""
        return ((self.__width * 2) + (self.__height * 2))
