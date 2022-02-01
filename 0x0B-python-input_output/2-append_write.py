#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """"""
    with open(filename, 'a+',) as f:
        f.write(text)
    return len(text)
