#!/usr/bin/env python3

"""
This code is a modified version of the solution provided by
u/goldjerrygold_cs. The general concensus was that this was
too hard for an easy challenge, requiring calculus.
"""


def derivative(xmin, xmax, y):
    n = len(y)
    width = 1. * (xmax - xmin) / (n-1)
    slopes = [(y[1] - y[0]) / width]
    if n == 2:
        return slopes
    for i in range(n-2):
        slopes.append((y[i+2] - y[i]) / (2. * width))
    slopes.append((y[n-1] - y[n-2]) / width)
    return slopes


def integral(xmin, xmax, y):
    n = len(y)
    width = 1. * (xmax - xmin) / (n-1)
    areas = [width * .5 * (y[0] + y[1])]
    for i in range(1, n-1):
        areas.append(areas[-1] + (width) * .5 * (y[i] + y[i+1]))
    return areas


print(derivative(xmin=-1, xmax=1, y=[-1.0, -.5, 0, .5, 1.0]))
print(integral(xmin=-1, xmax=1, y=[-1.0, -.5, 0, .5, 1.0]))
