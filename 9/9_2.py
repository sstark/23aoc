#!/bin/python

from sys import stdin
from itertools import pairwise, starmap
from functools import reduce
from operator import add


def sub(a, b):
    return b - a

def diffseq(arr):
    return list(starmap(sub, pairwise(arr)))

def nullseq(arr):
    return reduce(add, arr) == 0

res = 0
for line in stdin:
    seq = list(map(int, line.strip().split()))
    stack = [seq[0]]
    while True:
        if nullseq(seq):
            break
        seq = diffseq(seq)
        stack.append(seq[0])
    res += reduce(sub, reversed(stack))

print(res)
