#!/usr/bin/python3

from random import choice, randint
from sys import stdout

switch = 0
stick = 0

while True:
    # 3 doors, 1 contains the car
    doors = {1: False, 2: False, 3: False}
    doors[randint(1, 3)] = True

    # WLOG, contestant chooses door 1
    # Remove next door containing a goat
    for i in [2, 3]:
        if not doors[i]:
            del doors[i]
            break

    # If the first door is a car, stick won
    if doors[1]:
        stick += 1
    # Otherwise, car behind the other door and switch won
    else:
        switch += 1

    stdout.write("Switch {:0.4f}% vs ".format(100*switch/(switch+stick)))
    stdout.write("{:0.4f}% Stick\r\r".format(100*stick/(switch+stick)))
