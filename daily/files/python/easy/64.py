#!/usr/bin/env python3


def divisors(n):
    return [m+1 for m in range(n) if not n % (m+1)]


def divSum(n):
    return sum(divisors(n))


def divCount(n):
    return len(divisors(n))


def totatives(n):
    totatives = []
    for m in range(n):
        if [i for i in divisors(n) if i in divisors(m)] == [1]:
            totatives.append(m)
    return totatives


def totient(n):
    return len(totatives(n))


print(divisors(60))
print(divSum(60))
print(divCount(60))
print(totatives(30))
print(totient(30))
