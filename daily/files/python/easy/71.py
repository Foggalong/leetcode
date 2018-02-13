#!/usr/bin/env python3


def pythtrip(n):
    triples = []
    for i in range(1, n):
        for j in range(1, i):
            k = n - i - j
            if i**2 + j**2 == k**2:
                triples.append((i, j, k))
    return triples


print(pythtrip(504))
