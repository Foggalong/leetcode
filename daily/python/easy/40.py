#!/usr/bin/env python3


def f(x, y):
    (y + 1 - x) and (print("%s\n%s" % (x, x+1)) or f(x+2, y))


f(1, 1000)
