#!/usr/bin/python3

"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """A subclass inherited from class int."""
    def __eq__(self, other):
        """Special method that sets the behaviour of == """
        return int(self) != other

    def __ne__(self, other):
        """Special method that overrides the != operator."""
        return int(self) == other

