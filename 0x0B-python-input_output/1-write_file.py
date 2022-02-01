#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    
    with open(filename, "w") as f:
        f.write(text)

    lines = len(text)
    words = sum(len(line.split()) for line in text)
    characters = sum(len(line) for line in text)
    return characters
