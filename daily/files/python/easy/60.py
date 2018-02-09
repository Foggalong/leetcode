#!/usr/bin/env python3


def polite(n):
    y = []
    for j in range(n):
        x = []
        for i in range(n):
            if i+j > n:
                break
            s = sum(range(i+1, i+j+1))
            if s == n:
                x.append(range(i+1, i+j+1))
        y += x
    return y


print(polite(125))
