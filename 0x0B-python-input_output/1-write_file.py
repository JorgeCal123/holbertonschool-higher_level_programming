#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    with open(filename, "w") as f:
        f.write(text)
    f.closed
    return len(text)
