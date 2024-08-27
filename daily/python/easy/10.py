#!/usr/bin/env python3

number = input("Enter a number: ")
for char in number:
    if char in (str(i) for i in range(1, 10)):
        number = number.replace(char, "0")

formats = [
    "0000000000",
    "000-000-0000",
    "000.000.0000",
    "(000)000-0000",
    "(000) 000-0000",
    "000-0000"
]

if number in formats:
    print("Valid number")
else:
    print("Invalid number")
