#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rec1 = Rectangle(10, 2)
    print(rec1.id)

    rec2 = Rectangle(2, 10)
    print(rec2.id)

    rec3 = Rectangle(10, 2, 0, 0, 12)
    print(rec3.id)
