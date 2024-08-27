#!/usr/bin/env python3


def subset(A, N):
    if N == 1:
        return [[a] for a in A]
    return [[A[i]] + a for i in range(len(A)) for a in subset(A[i+1:], N-1)]


def powerset(A):
    output = [[]]
    for i in range(len(A)):
        output += subset(A, i)
    return {"".join(l) for l in output + [A]}


def substrings(n):
    alpha = [chr(97+i) for i in range(n)]
    return {"".join(l) for l in powerset(alpha)}


print(powerset("hello"))
print(substrings(5))
