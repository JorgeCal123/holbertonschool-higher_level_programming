#!/usr/bin/python3
def remove_char_at(str, n):
    b = n + 1
    msm = str[0 : n] + str[b : ]
    return ("{}".format(msm))
