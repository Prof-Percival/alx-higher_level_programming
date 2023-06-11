#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rec1 = Rectangle(10, 10, 10, 10)
    print(rec1)

    rec1.update(89)
    print(rec1)

    rec1.update(89, 2)
    print(rec1)

    rec1.update(89, 2, 3)
    print(rec1)

    rec1.update(89, 2, 3, 4)
    print(rec1)
 
    rec1.update(89, 2, 3, 4, 5)
    print(rec1) 
