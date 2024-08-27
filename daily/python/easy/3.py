#!/usr/bin/env python3

messg = input("What to encode? ").lower()
shift = int(input("What shift? "))
alpha = [chr(i) for i in range(97, 123)]
coded = ""

for letter in messg:
    if letter in alpha:
        coded += chr(((ord(letter) - 97 + shift) % 27) + 97)
    else:
        coded += letter

print(coded)
