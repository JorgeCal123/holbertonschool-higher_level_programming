#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = len(sys.argv)
    print("{:d} arguments:".format(lenght -1))
    for i in range(1, lenght):
        print(str(i) + ": "+ sys.argv[i])
