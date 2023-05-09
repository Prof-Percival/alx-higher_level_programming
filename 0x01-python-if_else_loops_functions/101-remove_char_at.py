#!/usr/bin/python3
def remove_char_at(string, n):
    s = ""
    for i in range(len(string)):
        if i != n:
            s = s + string[i]
    return (s)
