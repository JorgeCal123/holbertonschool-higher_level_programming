#!/usr/bin/python3
'''
add_integer


'''


def add_integer(a, b=98):
    """
    Method that is the addition of a and b
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    return (a + b)
