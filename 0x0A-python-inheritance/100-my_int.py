#!/usr/bin/python3

"""Write a class MyInt that inherits from Int"""


class MyInt(int):
    """Class MyInt inherited from int"""
    def __eq__(self, other):
        """Returns not equal """
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns equal"""
        return super().__eq__(other)
