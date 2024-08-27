#!/usr/bin/env python3

for i in range(1, int(input("Give an integer: "))+1):
    if not i % 15:
        print("FizzBuzz")
    elif not i % 5:
        print("Buzz")
    elif not i % 3:
        print("Fizz")
    else:
        print(i)
