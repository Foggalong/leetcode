#!/usr/bin/python3

string = "1-800-COMCAST"
number = ""

for char in string:
    if char in ["A", "B", "C"]:
        number += "2"
    elif char in ["D", "E", "F"]:
        number += "3"
    elif char in ["G", "H", "I"]:
        number += "4"
    elif char in ["J", "K", "L"]:
        number += "5"
    elif char in ["N", "M", "O"]:
        number += "6"
    elif char in ["P", "Q", "R", "S"]:
        number += "7"
    elif char in ["T", "U", "V"]:
        number += "8"
    elif char in ["W", "X", "Y", "Z"]:
        number += "9"
    else:
        number += char

print(number)
