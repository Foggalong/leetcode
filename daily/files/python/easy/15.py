#!/usr/bin/env python3

with open("15.py", "r") as file:
    lines = [line.strip() for line in file]

print("\n# Left Justify")
for line in lines:
    print(line)

maxline = max(len(line) for line in lines)
print("\n# Right Justify")
for line in lines:
    print(" "*(maxline-len(line)) + line)
