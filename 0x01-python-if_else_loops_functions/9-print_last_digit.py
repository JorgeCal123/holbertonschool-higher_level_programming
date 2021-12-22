#!/usr/bin/python3
def print_last_digit(number):
    R = 0
    if(number < 0):
        R = (-number % 10)
    else:
        R = (number % 10)
    print("{:d}".format(R), end="")
    return R
