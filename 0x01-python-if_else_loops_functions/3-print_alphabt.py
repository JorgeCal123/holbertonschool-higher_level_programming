#!/usr/bin/python3
for i in list(range(ord('a'), ord('z') + 1)):
    if (chr(i) != "q" and chr(i) != "e"):
        print("{}".format(chr(i)), end="")
