#!/usr/bin/python3
"""
function "Print Square"
"""


def print_square(size):
    """
    Print a perfect square given a valid int or float argument.
    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
