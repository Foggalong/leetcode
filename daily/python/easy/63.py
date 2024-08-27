#!/usr/bin/python3


def reverse(l, n):
    return l[n-1::-1] + l[n:]


A = [1, 2, 3, 4, 5]
print(reverse(A, 3))
