#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle data inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
