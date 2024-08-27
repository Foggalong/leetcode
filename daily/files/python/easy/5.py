#!/usr/bin/env python3

password = "ThisIsBadSecurity"

while True:
    attempt = input("What's the password? ")
    if attempt == password:
        with open("5.py", "r") as file:
            for line in file:
                print(line.strip())
        break
    else:
        print("Incorrect password!")
