#!/usr/bin/env python3


def palin(string):
    mid = int(len(string)/2)
    if len(string) % 2:
        if string[:mid] == string[mid+1:][::-1]:
            return True
        return False
    if string[:mid] == string[mid:][::-1]:
        return True
    return False


def prime(n):
    return not [i for i in range(2, int(1 + n**0.5)) if not n % i]


def emirp(n):
    return prime(n) and prime(int(str(n)[::-1])) and not palin(str(n))


n = int(input("n = "))
for i in range(2, n+1):
    if emirp(i):
        print(i)
