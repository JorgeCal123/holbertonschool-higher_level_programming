#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple = []
    l1 = list(tuple_a)
    l2 = list(tuple_b)
    while (len(l1) != 2 or len(l2) != 2):
        if (len(l1) >= len(l2)):
            l2.append(0)
        else:
            l1.append(0)

    for i in range(len(l1)):
        suma = l1[i] + l2[i]
        new_tuple.append(suma)
    return new_tuple
