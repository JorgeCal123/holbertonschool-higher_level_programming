#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0):
        return
    elif ((len(my_list) - 1) < idx):
        return
    else:
        return(my_list[idx])
