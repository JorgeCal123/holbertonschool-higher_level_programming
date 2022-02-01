#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """"function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
