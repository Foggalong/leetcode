#!/usr/bin/python3

c = input("What character? ")
n = int(input("How big? "))
r = input("Reversed? (y/n) ")
j = input("Right justified? (y/n) ")

if r == "y":
    vals = reversed(range(n))
elif r == "n":
    vals = range(n)

for i in vals:
    if j == "y":
        print(" "*(2**(n-1) - 2**i) + c*(2**i))
    elif j == "n":
        print(c*(2**i))
