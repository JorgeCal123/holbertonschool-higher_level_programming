#!/usr/bin/python3
"""Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square and Rectangle class """
    def __init__(self, size):
        """ Method constructor Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that return the area """
        return super().area()

    def __str__(self):
        """ method string """
        return "[Square] {}/{}".format(self.__size, self.__size)
