#!/usr/bin/env python3

from decimal import *
from functools import reduce
from operator import mul

# Set precission
getcontext().prec = 30


def prod(iterable):
    return reduce(mul, iterable, 1)


def term(n):
    """nth term of Euler series for pi/2"""
    num = prod(i+2 for i in range(n))
    den = prod((2*(i+1)+1) for i in range(n))
    return Decimal(num)/Decimal(den)


n, s = 1, Decimal(0)
while True:
    print(Decimal(2)*s)
    if s == s + term(n):
        break
    s += term(n)
    n += 1
