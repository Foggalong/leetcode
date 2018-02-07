#!/usr/bin/env python3

from re import split

line = max(split("[.!?]", input()), key=lambda x: len(x))
words = [w for w in line.split(" ") if len(w) > 4]

print(line, words)
