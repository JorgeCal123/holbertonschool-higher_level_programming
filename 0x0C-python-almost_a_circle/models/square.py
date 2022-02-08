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

    def update(self, *args, **kwargs):
        """method upsate"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """method to_dictionary"""
        return dict(id = self.id, x = self.x, size = self.size, y = self.y)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.heigh = value
