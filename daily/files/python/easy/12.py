#!/usr/bin/python3


def two(a): return [c+a.replace(c, "", 1) for c in list(a)]


string = input("String: ")
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

print(len(final), final)
