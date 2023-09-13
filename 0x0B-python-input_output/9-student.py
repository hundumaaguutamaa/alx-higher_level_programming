#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Represent a student."""

	def __init__(self, first_name, last_name, age):
        """Inistantiate a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

	def to_json(self):
        	"""Retrive a dictionary representation of the Student instance"""
        return self.__dict__
