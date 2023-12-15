#!/bin/python

from sys import stdin

val = 0
res = 0

for line in stdin:
    for c in line.strip():
        if c == ',':
            res += val
            val = 0
        else:
            val += ord(c)
            val *= 17
            val %= 256
    res += val

print(res)
