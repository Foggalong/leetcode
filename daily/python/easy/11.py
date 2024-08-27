#!/usr/bin/env python3

from datetime import date as d
print(d(int(input("Y ")), int(input("M ")), int(input("D "))).strftime("%A"))
