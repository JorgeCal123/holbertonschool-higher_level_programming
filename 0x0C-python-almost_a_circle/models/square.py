#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """method constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method str"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.heigh = value
