#!/usr/bin/env python3

from random import randint

print("You awaken to find yourself in a barren moor. Try 'look'")

while input("\n> ") != "look":
    print("Not yet!")

print("""
Grey foggy clouds float oppressively close to you, reflected in the murky
grey water which reaches up your shins. Some black plants barely poke out
of the shallow water. You notice a small watch-like device in your left
hand. It has hands like a watch, but the hands don't seem to tell time.
Try "north","south","east",or "west"
""")

cx, cy = randint(-50, 50), randint(-50, 50)
x, y = 0, 0

while (x, y) != (cx, cy):
    d = round(((cx-x)**2 + (cy-y)**2)**0.5, 2)
    print("The dial reads {}m".format(d))
    cmd = input("\n> ")

    if cmd == "north":
        y += 1
    elif cmd == "south":
        y -= 1
    elif cmd == "east":
        x += 1
    elif cmd == "west":
        x -= 1
    else:
        print("Enter a direction!")


print("You see a box sitting on the plane. Its filled with treasure!")
print("You win! The end.")
