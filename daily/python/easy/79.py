#!/usr/bin/env python3

def step_count(a, b, s):
    return [a + i*(b-a)/s for i in range(s+1)]
