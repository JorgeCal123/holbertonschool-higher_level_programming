#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            msm = ord(i) - 32
        else:
            msm = ord(i)
        print("{}".format(chr(msm)), end="")
    print()
