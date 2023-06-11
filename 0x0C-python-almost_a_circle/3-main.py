#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rec1 = Rectangle(3, 2)
    print(rec1.area())

    rec2 = Rectangle(2, 10)
    print(rec2.area())

    rec3 = Rectangle(8, 7, 0, 0, 12)
    print(rec3.area())
