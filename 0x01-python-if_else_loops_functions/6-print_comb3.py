#!/usr/bin/python3
aumento = 1
for i in range(0, 9):
    for j in range(aumento, 10):
        if(i == 8 and j == 9):
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
    aumento += 1
