#!/usr/bin/env python3

from sys import argv

with open(argv[1], "r") as file:
    text = "".join(line.strip() for line in file if line.strip()).lower()
    text = "".join(c for c in text if c in "abcdefghijklmnopqrstuvwxyz ")
    text = text.split(" ")

freq = {word: text.count(word) for word in text}

words = sorted(freq, key=lambda x: -freq[x])
for i in range(int(argv[2])):
    print(i+1, words[i], freq[words[i]])
