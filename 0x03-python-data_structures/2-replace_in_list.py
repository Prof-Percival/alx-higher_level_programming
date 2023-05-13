#!/usr/bin/python3
def replace_in_list(my_list, index, element):
    if index < 0:
        return (my_list)

    length = len(my_list)

    if index > length - 1:
        return (my_list)

    my_list[index] = element

    return (my_list)
