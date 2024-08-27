#!/usr/bin/env python3

lockers = [False]*1000
for j in range(1000):
    lockers = [not l if (i+1) % (j+1) else l for i, l in enumerate(lockers)]
print([i+1 for i, l in enumerate(lockers) if l])
