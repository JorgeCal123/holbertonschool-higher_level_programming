#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = len(sys.argv)
    if ((lenght - 1) == 1):
        print("{:d} argument:".format(lenght - 1))
    else:
        print("{:d} arguments:".format(lenght - 1))
    for i in range(1, lenght):
        print("{}: {}".format(i, sys.argv[i]))
