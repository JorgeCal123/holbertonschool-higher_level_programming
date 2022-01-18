#!/usr/bin/python3
"""Class Square"""


class Square:

    """Method constructor"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        return self._size * self._size

