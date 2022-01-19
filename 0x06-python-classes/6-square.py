#!/usr/bin/python3
"""Class Square"""


class Square:

    """Method constructor"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not isinstance(value[0], int) or
                not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._size * self._size

    def my_print(self):
        if (self._size == 0):
            print()
        for i in range(self._size):
            if (self._position[1] >= 0):
                for i in range(self._position[0]):
                    print(" ", end="")
            for j in range(self._size):
                print("{}".format("#"), end="")
            print()
