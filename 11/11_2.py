#!/bin/python

from sys import stdin
from itertools import combinations, starmap

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def expand(g):
    out = []
    xvals = sorted([x[0] for x in g])
    yvals = sorted([x[1] for x in g])
    xgaps = set(range(xvals[-1])) - set(xvals)
    ygaps = set(range(yvals[-1])) - set(yvals)
    for galaxy in g:
        x = galaxy[0]
        y = galaxy[1]
        for xgap in reversed(sorted(xgaps)):
            if xgap < x:
                x += 999999
        for ygap in reversed(sorted(ygaps)):
            if ygap < y:
                y += 999999
        out.append((x, y))
    return out

galaxies = []
y = 0
for line in stdin:
    x = 0
    for c in line.strip():
        if c == '#':
            galaxies.append((x, y))
        x += 1
    y += 1

galaxies = expand(galaxies)
print(sum(starmap(dist, combinations(galaxies, 2))))
