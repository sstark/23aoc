#!/bin/python

from sys import stdin
from itertools import combinations, starmap

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def expand(l, by=1):
    out = []
    gaps = set(range(l[-1])) - set(l)
    for e in l:
        for gap in reversed(sorted(gaps)):
            if gap < e:
                e += by
        out.append(e)
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

galaxies = zip(
    expand(sorted([x[0] for x in galaxies]), by=999999),
    expand(sorted([x[1] for x in galaxies]), by=999999)
)
print(sum(starmap(dist, combinations(galaxies, 2))))
