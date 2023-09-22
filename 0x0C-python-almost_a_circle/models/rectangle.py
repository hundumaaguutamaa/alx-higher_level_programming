#!/usr/bin/python3

"""Inheriting from a class Base."""


from models.base import Base


class Rectangle(Base):
    """ A subclass Rectangle inherited from Base class. """
    def __init__(self, width, height, x=0, y=0, id=None):
        
        """Call the super class with id."""
        super().__init__(id)
        
        """Initializing instances."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        

    @property
    def width(self):
        """Retrive the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting and validating width attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        
        if value <= 0:
            raise ValueError("width must be > 0")
       
        self.__width = value

    @property
    def height(self):
        """Retrive height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """setting and validating height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        
        self.__height = value

    @property
    def x(self):
        """Retrieve x."""
        return self.__x

    @x.setter
    def x(self, value):
        """setting and validating x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        
        self.__x = value

    @property
    def y(self):
        """Retrieve y."""
        return self.__y

    @y.setter
    def y(self, value):
        """setting and validating y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        
        self.__y = value

    def area(self):
        """Return Area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """print charater # to the stdout."""
        print('\n' * self.__y, end='')
        for _ in range(self.__height):
          print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """"overriding __str__ method."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """"Add public method an assigns an argument to each attribute."""
        update_arg = ["id", "width", "height", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, update_arg[i], args[i])
        else:
            for h in kwargs:
                setattr(self, h, kwargs[h])

    def to_dictionary(self):
        """Returns dict representation of a Rectangle."""

        return {
            
            "x": self.x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            'width': self.__width,

        }
