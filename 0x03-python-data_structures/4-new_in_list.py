#!/usr/bin/python3
def new_in_list(my_list, index, element):
    length = len(my_list)

    new_list = my_list[:]

    if 0 <= index < length:
        new_list[index] = element

    return (new_list)
