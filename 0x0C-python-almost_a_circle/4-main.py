#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rec1 = Rectangle(4, 6)
    rec1.display()

    print("---")

    rec1 = Rectangle(2, 2)
    rec1.display()
