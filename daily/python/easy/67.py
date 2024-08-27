#!/usr/bin/env python3


def rev32(n):
    return int("{0:032b}".format(n)[::-1], 2)


print(rev32(13))
