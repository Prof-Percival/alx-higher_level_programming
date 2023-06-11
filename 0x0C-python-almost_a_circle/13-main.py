#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    square1 = Square(10, 2, 1)
    print(square1)
    square1_dictionary = square1.to_dictionary()
    print(square1_dictionary)
    print(type(square1_dictionary))

    square2 = Square(1, 1)
    print(square2)
    square2.update(**square1_dictionary)
    print(square2)
    print(square1 == square2)
