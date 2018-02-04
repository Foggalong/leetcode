#!/usr/bin/env python3

x, k = [12, 24, 32, 44, 55, 66, 75], 4
blocks = [x[i*k:(i+1)*k] for i in range(int(len(x)/k))] + [x[(len(x) // k)*k:]]
print([i for r in (list(reversed(b)) for b in blocks) for i in r])
