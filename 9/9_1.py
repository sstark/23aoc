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
    res += seq[-1]
    while not nullseq(seq):
        seq = diffseq(seq)
        res += seq[-1]

print(res)
