#!/usr/bin/python3

year = int(input("Year: "))

print("Century", int((year-1)/100)+1)

if year % 4:
    print("Not a leap year")
elif year % 100:
    print("It's a leap year")
elif year % 400:
    print("Not a leap year")
else:
    print("It's a leap year")
