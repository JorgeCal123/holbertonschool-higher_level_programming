#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """functions area()"""

    def area(self):
        """Function area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function integer_validator"""

        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
