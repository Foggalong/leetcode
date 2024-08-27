#!/usr/bin/env python3


def titlecase(string, exceptions):
    words = string.lower().split(" ")
    title = words.pop(0).title() + " "
    title += " ".join(w if w in exceptions else w.title() for w in words)
    return title


exceptions = ['are', 'is', 'in', 'your', 'my']
print(titlecase('THE vitamins ARE IN my fresh CALIFORNIA raisins', exceptions))
