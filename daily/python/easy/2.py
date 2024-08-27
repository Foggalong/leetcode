#!/usr/bin/env python3

F = input("What's the force? (N) ")
M = input("What's the mass? (kg) ")
A = input("What's the acceleration? (m/s^2) ")

if "??" in "".join(str(a) for a in sorted([F, M, A])):
    print("You must have at least two knowns!")
elif F == "?":
    print("Force is", float(M)*float(A), "N")
elif M == "?":
    print("Mass is", float(F)/float(A), "kg")
elif A == "?":
    print("Acceleration is", float(F)/float(M), "m/s^2")
