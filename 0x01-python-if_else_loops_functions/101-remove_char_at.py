#!/usr/bin/python3
def remove_char_at(str, n):
    b = n + 1
    if n >= 0:
        str = str[:n] + str[b:]
    return ("{}".format(str))
