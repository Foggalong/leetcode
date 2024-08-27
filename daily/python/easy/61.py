#!/usr/bin/env python3


def binrot(n):
    s = "{0:b}".format(n)
    if s[-1] == 0:
        return int(s[:-1], 2)
    return int(s[-1] + s[:-1], 2)


n = int(input("n = "))
seq = [str(n)]
while binrot(n) != n:
    n = binrot(n)
    seq.append(str(n))
print(" -> ".join(seq))
