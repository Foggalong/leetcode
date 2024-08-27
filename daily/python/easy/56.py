#!/usr/bin/env python3

s = ""
for i in range(26):
    s = s+chr(i+97)+s

with open("56.txt", "w+") as file:
    file.write(s)
