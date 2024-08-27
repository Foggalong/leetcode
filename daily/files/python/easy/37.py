#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as file:
    lines = [line.strip() for line in file]
    words = " ".join(lines).split(" ")
print("{} lines and {} words".format(len(lines), len(words)))
