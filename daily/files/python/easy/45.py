#!/usr/bin/env python3

a = "░"
b = "▓"

[n, m, l] = [int(x) for x in input().split(",")]

o = [a*2*l if (i+1) % 2 else b*2*l for i in range(n)]
e = [b*2*l if (i+1) % 2 else a*2*l for i in range(n)]
rows = [o if (i+1) % 2 else e for i in range(m) for j in range(l)]

for row in rows:
    print("".join(row))
