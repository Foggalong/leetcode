#!/usr/bin/env python3

from random import choice
from time import time

score = 0
cards = {
    # Question : Answer
    "Äpfel": "apples",
    "beginnen": "begin",
    "beginnst": "start",
    "Berg": "mountain",
    "Bürger": "citizen",
    "danke": "thanks",
    "fahren": "drives",
    "Gärten": "gardens",
    "hallo": "hello",
    "Kinder": "child",
    "Kuchen": "cake",
    "Küche": "kitchen",
    "nitch": "not",
    "Nudeln": "pasta",
    "oder": "or",
    "schläfst": "sleep",
    "Steckdose": "plug socket",
    "Taschen": "bags",
    "trinkt": "drinks",
    "traurig": "sad",
    "Urgroßmutter": "great-grandmother",
    "Zahn": "tooth",
}

while True:
    print("\nScore: {}".format(score))
    qn, t = choice(list(cards.keys())), time()
    ans = input("What is '{}'?\n".format(qn))
    if ans == "exit":
        break
    elif ans == cards[qn]:
        taken = 6 - int(time() - t)
        if taken > 1:
            score += taken
        else:
            score += 1
        print("Correct!")
    else:
        print("Incorrect! The answer was '{}'".format(cards[qn]))
