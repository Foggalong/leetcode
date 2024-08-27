#!/usr/bin/env python3

with open("../../data/easy80.txt", "r") as file:
    words = [line.strip() for line in file]

anagrams = {}

for word in words:
    chars = "".join(sorted(word))
    if chars in anagrams.keys():
        anagrams[chars].append(word)
    else:
        anagrams[chars] = [word]

print(sorted(anagrams.values(), key=lambda x: -len(x[:]))[0])
print(sorted(anagrams.values(), key=lambda x: -len(x[:]))[1])
