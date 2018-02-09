#!/usr/bin/env python3

# Given a list of n real numbers, a real number t, and an integer k,
# determine if there exists a k-element subset of the original list
# of n real numbers that is which has a sum less than t.


def subset(A, N):
    if N == 1:
        return [[a] for a in A]
    return [[A[i]] + a for i in range(len(A)) for a in subset(A[i+1:], N-1)]


def ullman(A, t, k):
    return bool([a for a in subset(A, k) if sum(a) < t])


# The above is the niave way of solving this problem. It's good in that it
# makes it quite explicit what's going on, but there's a mathematical way
# to approach it which gives a much simpler solution.

# Given a list of real numbers A, the k-element subset of A with the smallest
# sum of elements will be precisely the smallest k elements in A. This the
# Ullman puzzle is true if t is less than the sum of the k smallest elements.

def ullman2(A, t, k):
    return sum(sorted(A)[:k]) < t


A = [1, 2, 3, 4]
print(ullman(A, 3, 2), ullman2(A, 3, 2))
print(ullman(A, 3.4, 2), ullman2(A, 3.4, 2))
