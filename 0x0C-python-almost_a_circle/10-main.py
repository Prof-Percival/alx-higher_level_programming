#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    square1 = Square(5)
    print(square1)
    print(square1.size)
    square1.size = 10
    print(square1)

    try:
        square1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

