#!/usr/bin/python3
"""method say_my_name"""


def say_my_name(first_name, last_name=""):
    """message with the name complete"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    if last_name == "":
        print("My name is {:s} ".format(first_name))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
