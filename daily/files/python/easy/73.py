#!/usr/bin/env python3

string = "2 4 * 6 2 - + 5 /"

inputs = string.split(" ")
memory = []

for char in inputs:
    if char in ["+", "*", "-", "/"]:
        y = memory.pop(-1)
        x = memory.pop(-1)
        memory.append(str(eval(x+char+y)))
    else:
        memory.append(char)

print(memory[0])
