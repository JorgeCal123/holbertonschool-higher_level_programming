#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    """class docstr"""

    def __eq__(self, value):
        """method eq"""
        return self.real != value

    def __ne__(self, value):
        """method ne"""
        return self.real == value
