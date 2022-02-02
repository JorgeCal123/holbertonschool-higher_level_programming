#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""
    with open(filename, 'a+',) as f:
        f.write(text)
    return len(text)
