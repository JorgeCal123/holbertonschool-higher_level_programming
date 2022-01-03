#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if (idx < 0):
        return copy
    elif ((len(my_list) - 1) < idx):
        return copy
    else:
        copy[idx] = element
        return copy

