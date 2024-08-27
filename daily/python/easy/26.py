#!/usr/bin/env python3

string = "Hello, world!"

output = ""
dupes = ""
for char in string:
    if char in output:
        dupes += char
    else:
        output += char

print(output, dupes)
