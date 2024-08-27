#!/usr/bin/env python3

from random import randint

iterations = int(input("Iterations: "))
rulenumber = int(input("Rule: "))


def disp(array, i):
    index = str(i+1).zfill(len(str(iterations)))
    print(index, "|", "".join("▓▓" if int(a) else "░░" for a in array))


array = [randint(0, 1) for _ in range(25)]
keys = ["111", "110", "101", "100", "011", "010", "001", "000"]
states = list(str("{0:08b}".format(rulenumber)))
rule = dict(zip(keys, states))

for i in range(iterations):
    disp(array, i)
    for j in range(len(array)):
        window = "".join(str(array[k % len(array)]) for k in [j-1, j, j+1])
        array[j] = rule[window]
