#!/usr/bin/env python3


def decode(s):
    return sum((ord(c)-65)*(26**i) for i, c in enumerate(reversed(s)))


def encode(n):
    x = [n]
    while x[-1] > 25:
        y = 0
        while x[-1] > 25:
            x[-1] -= 26
            y += 1
        x.append(y)
    return "".join(chr(c+65) for c in x)[::-1]


print(encode(decode("CSGHJ")*decode("CBA")))
