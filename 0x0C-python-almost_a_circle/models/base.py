#!/usr/bin/python3
"""Class Base"""


class Base:
    """Class father"""

    __nb_objects = 0

    def __init__(self, id=None):
        """method constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
