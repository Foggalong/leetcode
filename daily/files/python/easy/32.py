#!/usr/bin/env python3

# TODO: extra credit in this challenge was to add further betting options.
# See https://en.wikipedia.org/wiki/Roulette for more info.

from random import choice

table = [str(i) for i in range(0, 37)] + ["00"]
money = 10

while money > 0:
    print("\nMoney £{0:.2f}".format(money))
    [bet, space] = input("Place your bet: ").split(" on ")
    money -= float(bet)

    landed = choice(table)
    if space == landed:
        wins = 35*float(bet)
        print("Ball on {0}. You won £{1:.2f}!".format(landed, wins))
        money += wins
    else:
        print("Ball on {}. You lost!".format(landed))

print("Uh oh, you're out of money!")
