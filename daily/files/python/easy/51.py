#!/usr/bin/env python3


def subset(A, N):
    if N == 1:
        return [[a] for a in A]
    return [[A[i]] + a for i in range(len(A)) for a in subset(A[i+1:], N-1)]


A = [1, 2, 3, 4, 5]
N = 3
print(subset(A, N))
