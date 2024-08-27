#!/usr/bin/env python3

animals = {
    "cow": "moo",
    "chicken": "cluck",
    "turkey": "gobble",
    "kangaroo": "g'day",
    "t-rex": "RAWR",
    "python": "ssss"
}

p = ["Old McDonald had a deformed farm, ", "ee-i-ee-i-o"]

for a, s in animals.items():
    print(p[0]+p[1]+",")
    print("And on that farm he had a {}, {}.".format(a, p[1]))
    print("With a {0} {0} here and a {0} {0} there,".format(s))
    print("Here a {0} there a {0} everwhere {0} {0},".format(s))
    print(p[0]+p[1]+".\n")
