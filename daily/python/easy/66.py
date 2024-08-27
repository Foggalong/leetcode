#!/usr/bin/env python3


def romanLT(x, y):
    for n in ["M", "D", "C", "L", "X", "V", "I"]: 
        if x.count(n) < y.count(n):
            return True
        if y.count(n) < x.count(n):
            return False
    return False


s1 = "MXII"
s2 = "MXVII"
print(romanLT(s1, s2))
