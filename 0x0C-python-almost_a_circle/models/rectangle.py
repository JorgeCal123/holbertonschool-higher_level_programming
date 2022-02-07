#!/usr/bin/python3
"""Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """method area"""
        return self.width * self.height

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width{}".format(" must be an integer"))
        if value <= 0:
            raise ValueError("width {}".format("must be > 0"))

        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height{}".format(" must be an integer"))
        if value <= 0:
            raise ValueError("height {}".format("must be > 0"))

        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x{}".format(" must be an integer"))
        if value < 0:
            raise ValueError("x {}".format("must be >= 0"))
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y{}".format(" must be an integer"))
        if value < 0:
            raise ValueError("y {}".format("must be >= 0"))

        self.__y = value
