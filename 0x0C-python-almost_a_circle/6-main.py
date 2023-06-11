#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rec1 = Rectangle(2, 3, 2, 2)
    rec1.display()

    print("---")

    rec2 = Rectangle(3, 2, 1, 0)
    rec2.display()
