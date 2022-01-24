#!/usr/bin/python3

"""class Rectangle"""


class Rectangle:
    """Rectangle class defined by width and height."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        rectangle = ""

        if (self.height == 0 or self.width == 0):
            return rectangle

        for i in range(self.height):
            for j in range(self.width):
                rectangle = rectangle + str(self.print_symbol)
            if (i < self.height - 1):
                rectangle = rectangle + "\n"
        return rectangle

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        if Rectangle.number_of_instances >= 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
