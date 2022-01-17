#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    j = 0

    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{}".format(my_list[i]), end="")
                j += 1
        except TypeError as err:
            print(err)
    print();
    return (j)
