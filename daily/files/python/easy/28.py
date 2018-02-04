#!/usr/bin/python3

# If you are given an array with integers between 1 and 1,000,000 or in some
# other interval and one integer is in the array twice. How can you determine
# which one? What's the most efficient way to do this?

from random import randint, shuffle
from time import time

# This is setup of the question, not part of the solution
array = list(range(1, 1000001)) + [randint(1, 1000000)]
shuffle(array)

t = time()
done, i = {}, 0
for x in array:
    if x in done:
        print("{} is duplicated at {} and {}".format(x, i, done[x]))
    done[x] = i
    i += 1
print("Took", round(time()-t, 2), "seconds")
