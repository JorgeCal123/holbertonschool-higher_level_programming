#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = len(sys.argv)
    suma = 0
    for i in range(1, lenght):
        suma+=int(sys.argv[i])
    print(suma)
