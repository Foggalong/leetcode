#!/usr/bin/env python3

from os import remove
from urllib.request import urlretrieve

url = "https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/dotnetperls-controls/enable1.txt"
urlretrieve(url, "words.txt")

with open ("words.txt", "r") as file:
    words = [line.strip() for line in file]
remove("words.txt")

anagrams = {}

for word in words:
    chars = "".join(sorted(word))
    if chars in anagrams.keys():
        anagrams[chars].append(word)
    else:
        anagrams[chars] = [word]

print(sorted(anagrams.values(), key=lambda x: -len(x[:]))[0])
print(sorted(anagrams.values(), key=lambda x: -len(x[:]))[1])

