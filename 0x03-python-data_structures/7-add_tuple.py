#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    l1 = list(tuple_a)
    l2 = list(tuple_b)
    while (len(l1) != 2 or len(l2) != 2):
        if (len(l2) < 2):
            l2.append(0)
        elif(len(l1) < 2):
            l1.append(0)

    new_tuple = (l1[0] + l2[0], l1[1] + l2[1])
    return new_tuple
