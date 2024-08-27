#!/usr/bin/env python3


def encode(n, b):
    x = [n]
    while x[-1] > b-1:
        y = 0
        while x[-1] > b-1:
            x[-1] -= b
            y += 1
        x.append(y)
    return "".join(str(c) if c < 10 else chr(c+55) for c in x[::-1])


def palin(string):
    mid = int(len(string)/2)
    if len(string) % 2:
        if string[:mid] == string[mid+1:][::-1]:
            return True
        return False
    if string[:mid] == string[mid:][::-1]:
        return True
    return False


for i in range(2, 37):
    m = encode(10858, i)
    if palin(str(m)):
        print("{} = {} ({})".format(10858, m, i))
