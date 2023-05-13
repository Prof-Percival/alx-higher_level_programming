#!/usr/bin/python3
def delete_at(my_list=[], index=0):
    length = len(my_list)

    if index < 0 or index >= length:
        return (my_list)

    del my_list[index]

    return (my_list)
