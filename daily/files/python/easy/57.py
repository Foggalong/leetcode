#!/usr/bin/env python3


def subset(A, N):
    if N == 1:
        return [[a] for a in A]
    return [[A[i]] + a for i in range(len(A)) for a in subset(A[i+1:], N-1)]


def powerset(A):
    output = [[]]
    for i in range(len(A)):
        output += subset(A, i)
    return output + [A]


def maxsubsum(A):
    return max(powerset(A), key=lambda x: sum(i for i in x))


A = [1, -2, 3, -4, 5]
print(maxsubsum(A))
