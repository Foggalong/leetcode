#!/usr/bin/env python3

from time import sleep
from sys import stdout

alpha = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}
morse = {a: b for b, a in alpha.items()}


def encode(string):
    code = []
    for char in string.upper():
        if char in list(alpha.keys()):
            code.append(alpha[char.upper()])
    return " ".join(code)


def decode(string):
    mssg = ""
    for seq in string.split(" "):
        mssg += morse[seq]
    return mssg


def display(morse):
    stdout.write("  \r")
    for char in morse:
        sleep(0.2)
        if char == ".":
            stdout.write("■ \r")
            sleep(0.2)
            stdout.write("  \r")
        elif char == "-":
            stdout.write("■ \r")
            sleep(0.6)
            stdout.write("  \r")
        elif char in [" ", "/"]:
            stdout.write("  \r")
            sleep(0.2)
    pass


display(encode("Hello, world!"))
