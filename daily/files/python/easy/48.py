#!/usr/bin/python3

from random import randint

array = [randint(1, 100) for _ in range(10)]
array.sort(key=lambda x: x % 2)

# Alternate explicit implementation
# for i in range(len(array)):
#    if not array[i] % 2:
#        array.insert(0, array[i])
#        array.pop(i+1)
