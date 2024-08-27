#!/usr/bin/python3

n = [1, 2, 3, 4, 5]
t = 6

pairs = [(n[i], n[j]) for i in range(len(n)) for j in range(i, len(n))]
solns = [p for p in pairs if p[0] + p[1] == t]
print(solns)
