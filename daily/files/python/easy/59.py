#!/usr/bin/env python3

s = "Double, double, toil and trouble"
t = "il an"

for i in range(len(s)):
    if s[i:i+len(t)] == t:
        print(i)
