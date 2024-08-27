#!/usr/bin/env python3


def morse(X):
    codes = []
    strings = ["-", "."]
    while strings:
        s = strings.pop(0)
        length = s.count(".") + s.count("-")*2
        if length < X:
            strings.append(s+".")
            strings.append(s+"-")
        elif length == X:
            codes.append(s)
    return codes


print("\n".join(morse(35)))
