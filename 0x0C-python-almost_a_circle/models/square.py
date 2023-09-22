#!/usr/bin/python3

"""Write a child class Square inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Subclass of class Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)
        """Calling superclass attributes."""
        self.size = size

    def __str__(self):
        """Returns a string representation of a square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Retrieve attribute from class Rectangle."""
        return self.width

    @size.setter
    def size(self, value):
        """Validation values for Rectangle."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        elif kwargs:
            for attribute, value in kwargs.items():
                if hasattr(self, attribute):
                    setattr(self, attribute, value)

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle."""
        return {
            
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
            
            }
