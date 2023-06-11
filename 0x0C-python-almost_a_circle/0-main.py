#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    base1 = Base()
    print(base1.id)

    base2 = Base()
    print(base2.id)

    base3 = Base()
    print(base3.id)

    base4 = Base(12)
    print(base4.id)

    base5 = Base()
    print(base5.id)
