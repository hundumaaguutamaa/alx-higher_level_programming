#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Representing a square."""
    
    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): Size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get,set current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square, current area."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the equals to comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the not equal comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define lessthan comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the lessthan or equal comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the greaterthan comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the greaterthan or equal compmarison to a Square."""
        """Return area"""
        return self.area() >= other.area()
