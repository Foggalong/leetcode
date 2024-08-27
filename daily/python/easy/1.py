#!/usr/bin/env python3

name = input("What's your name? ")
age = input("How old are you? ")
user = input("What's your Reddit username? ")

with open("data.txt", "w+") as file:
    file.write(",".join([name, age, user]))

reply = "Your name is {}, you are {} years old, and your username is {}"
print(reply.format(name, age, user))
