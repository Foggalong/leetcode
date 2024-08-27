#!/usr/bin/env python3

words = ["shoe", "hat"]
words.sort(key=lambda x: sum(ord(c) for c in x))
print(words)
