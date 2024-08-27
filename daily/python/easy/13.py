#!/usr/bin/env python3


def dayno(m, d, leap=False):
    if not leap:
        return sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m-1]) + d
    return sum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m-1]) + d


print(dayno(6, 24))
print(dayno(6, 24, True))
