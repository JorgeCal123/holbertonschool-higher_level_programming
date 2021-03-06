#!/usr/bin/python3

"""
text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: "., ?" 
    """
    delim = ".?:"
    i = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    while i < len(text):
        print(text[i], end="")
        if text[i] in delim:
            print("\n")
            i += 2
        else:
            i += 1
