#!/bin/python

from sys import stdin
from itertools import combinations, starmap

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def expand(l, by=1):
    gaps = set(range(sorted(l)[-1])) - set(l)
    for e in l:
        for gap in reversed(sorted(gaps)):
            if gap < e:
                e += by
        yield e

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
    expand([x[0] for x in galaxies], by=999999),
    expand([x[1] for x in galaxies], by=999999)
)
print(sum(starmap(dist, combinations(galaxies, 2))))
