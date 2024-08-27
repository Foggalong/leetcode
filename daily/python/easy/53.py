#!/usr/bin/python3


def merge(a, b):
    c = []
    while a+b:
        if a[0] < b[0]:
            c.append(a[0])
            del a[0]
        else:
            c.append(b[0])
            del b[0]
        if not a:
            c += b
            b = []
        elif not b:
            c += a
            a = []
    return c


a = [1, 5, 7, 8]
b = [2, 3, 4, 7, 9]

print(merge(a, b))
