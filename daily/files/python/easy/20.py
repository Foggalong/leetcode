#!/usr/bin/env python3

primes = []
for n in range(2, 2000):
    if all(n % p != 0 for p in primes):
        primes.append(n)

print(primes)
