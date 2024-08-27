#!/usr/bin/env python3


def credit(L, C):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] + L[j] == C:
                return "{},{}".format(i+1, j+1)


L = [5, 75, 25]
C = 100
print(L, C)
print(credit(L, C))

L = [150, 24, 79, 50, 88, 345, 3]
C = 200
print(L, C)
print(credit(L, C))

L = [2, 1, 9, 4, 4, 56, 90, 3]
C = 8
print(L, C)
print(credit(L, C))
