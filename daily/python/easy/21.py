#!/usr/bin/env python3

"""
Note that the functions two(a) and perms(string) are from the
solution to 12.py for finding all the permutations of a given
string. Python can't import from files with integer filenames
"""


def two(a): return [c+a.replace(c, "", 1) for c in list(a)]


def perms(string):
    combs = two(string)

    for i in range(1, len(string)):
        old = combs
        combs = []
        for s in old:
            combs += [s[:i]+t for t in two(s[i:])]

    final = []
    for i in combs:
        if i not in final:
            final.append(i)
    return(final)


print(sorted(perms(input("Give a number: ")))[-1])
