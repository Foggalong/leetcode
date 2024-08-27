#!/usr/bin/env python3

A = [4, 3, 2, 1, 5, 7]
k = 3

print([min(A[i:i+k]) for i in range(len(A)-k+1)])
