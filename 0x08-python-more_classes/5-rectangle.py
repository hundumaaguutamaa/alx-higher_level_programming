#!/usr/bin/python3

"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """Class Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        

    @property
    def width(self):
        """Retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Get area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Get Rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Print behavior of the Rectangle object."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Sets delete behavior of the Rectangle object."""
        print("Bye rectangle...")
