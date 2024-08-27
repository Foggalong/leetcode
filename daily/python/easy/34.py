#!/usr/bin/env python3

from sys import argv

print(sum(int(i)**2 for i in sorted(argv[1:])[1:]))
