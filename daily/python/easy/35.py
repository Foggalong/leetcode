#!/usr/bin/env python

n = 120
i = 1
s = 0
lines = []

while s+i <= n:
    lines.append([str(x) for x in list(range(1, n+1))[s:s+i]])
    s += i
    i += 1

for line in lines[::-1]:
    print(" ".join([x.zfill(len(str(lines[-1][-1]))) for x in line]))
