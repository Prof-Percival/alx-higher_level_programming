#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    square1 = Square(5)
    print(square1)

    square1.update(10)
    print(square1)

    square1.update(1, 2)
    print(square1)

    square1.update(1, 2, 3)
    print(square1)

    square1.update(1, 2, 3, 4)
    print(square1)

    square1.update(x=12)
    print(square1)

    square1.update(size=7, y=1)
    print(square1)

    square1.update(size=7, id=89, y=1)
    print(square1)
