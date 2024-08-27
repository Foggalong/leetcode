#!/usr/bin/env python3

words = input().split(" ")

lines = []
while words:
    line = ""
    while words and len(line + words[0]) < 20:
        line += " " + words[0]
        words.pop(0)
    lines.append(line)

print("*"*25 + "\n*" + " "*23 + "*")
for line in lines:
    pad = " " * (int((20-len(line))/2) + 1)
    if len(line) % 2:
        print("*" + pad + line + pad + "  *")
    else:
        print("*" + pad + line + pad + " *")
print("*" + " "*23 + "*\n" + "*"*25)
