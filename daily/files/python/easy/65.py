#!/usr/bin/env python3

x = round(float(12.33), 2)
bill = [100, 50, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
comp = [0]*len(bill)

for b in range(len(bill)):
    while x > bill[b]:
        comp[b] += 1
        x -= bill[b]

print(comp)
