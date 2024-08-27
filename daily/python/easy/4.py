#!/usr/bin/env python3

from random import randint

m = int(input("What length passwords? "))
for n in range(int(input("How many passwords? "))):
    print("".join(chr(randint(33, 127)) for i in range(m)))
