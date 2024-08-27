#!/usr/bin/env python3

from time import sleep
from sys import stdout

for i in range(0, 99):
    l1 = "{0} bottles of beer on the wall, {0} bottles of beer.           \r"
    stdout.write(l1.format(99-i))
    sleep(2.8)
    l2 = "Take one down, pass it around, {} bottles of beer on the wall. \r"
    stdout.write(l2.format(98-i))
    sleep(3.3)
