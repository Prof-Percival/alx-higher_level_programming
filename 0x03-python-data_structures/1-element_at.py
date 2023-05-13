#!/usr/bin/python3
def element_at(my_list, index):
    if index < 0:
        return (None)

    length = len(my_list)

    if index > length - 1:
        return (None)

    return(my_list[index])
