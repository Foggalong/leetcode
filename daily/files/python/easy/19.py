#!/usr/bin/python3

from os import remove
from urllib.request import urlretrieve

url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"
urlretrieve(url, "book.txt")

with open("book.txt", "r") as file:
    lines = [line.strip().lower() for line in file]
remove("book.txt")

# Cut out header and footer
lines = lines[61:12681]

# Chapter titles
chaps = [
    "I. A Scandal in Bohemia",
    "II. The Red-headed League",
    "III. A Case of Identity",
    "IV. The Boscombe Valley Mystery",
    "V. The Five Orange Pips",
    "VI. The Man with the Twisted Lip",
    "VII. The Adventure of the Blue Carbuncle",
    "VIII. The Adventure of the Speckled Band",
    "IX. The Adventure of the Engineer's Thumb",
    "X. The Adventure of the Noble Bachelor",
    "XI. The Adventure of the Beryl Coronet",
    "XII. The Adventure of the Copper Beeches"
]

# Cut out chapter titles
story = ""
for line in lines:
    if not any(chap.lower() in line for chap in chaps):
        story += line

# Do frequency analysis
counts = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz0123456789"}
for char in story:
    if char in counts:
        counts[char] += 1

for x in counts:
    print(x, counts[x], str(round(100*counts[x]/sum(counts.values()), 2))+"%")
