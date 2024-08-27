#!/usr/bin/python3


def dupes(a, b):
    return "".join([c if c not in b else "" for c in a])


print(dupes("Daily Programmer", "aeiou "))
