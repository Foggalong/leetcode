#!/usr/bin/env python3

n = str(input("> "))

shortscale = ["", "thousand", "million", "billion", "trillion",
              "quadrillion", "quintillion", "sextillion"]
longscale = ["", "thousand", "million", "milliard", "billion",
             "billiard", "trillion", "trilliard"]

shortans = []
longans = []

i = 0
while len(n) > 3:
    shortans.insert(0, n[-3:] + " " + shortscale[i])
    longans.insert(0, n[-3:] + " " + longscale[i])
    n = n[:-3]
    i += 1
shortans.insert(0, n + " " + shortscale[i])
longans.insert(0, n + " " + longscale[i])

print("Short scale:", ", ".join(shortans))
print("Long scale:", ", ".join(longans))
