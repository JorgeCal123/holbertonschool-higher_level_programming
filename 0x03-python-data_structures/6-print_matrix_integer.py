#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if (i != 0):
            print()
        for j in range(len(matrix[0])):
            print("{:d}".format(matrix[i][j]), end="")
            if(j != (len(matrix[0]) - 1)):
                print("", end=" ")
    print()
