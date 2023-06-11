#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    square1 = Square(5)
    print(square1)
    print(square1.area())
    square1.display()

    print("---")

    square2 = Square(2, 2)
    print(square2)
    print(square2.area())
    square2.display()

    print("---")

    square3 = Square(3, 1, 3)
    print(square3)
    print(square3.area())
    square3.display()
