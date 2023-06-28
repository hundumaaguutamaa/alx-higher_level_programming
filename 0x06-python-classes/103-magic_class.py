#!/usr/bin/python3

"""Define python MagicClass to do as the same bytecode provided"""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass with radius.

    Arg:
            radius (float or int):radius of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
