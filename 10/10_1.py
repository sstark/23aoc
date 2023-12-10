#!/bin/python

from sys import stdin
from io import StringIO

# cardinal points as unit vectors
N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)

ctrl = {
    '|': [N, S],
    '-': [E, W],
    'L': [N, E],
    'J': [N, W],
    '7': [S, W],
    'F': [S, E],
}

# The map as a hash of ctrl characters
# using coordinate tuples as the keys
class PipeMap():

    def __init__(self):
        self.map = {}
        y = 0
        for line in stdin:
            x = 0
            for char in line.strip():
                self.map[(x, y)] = char
                x += 1
            y += 1
        self.width = x
        self.height = y

    def __str__(self):
        out = StringIO()
        for y in range(self.height):
            for x in range(self.width):
                out.write(self.map[(x, y)])
            out.write('\n')
        return out.getvalue()

    def find_start(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[(x, y)] == 'S':
                    return (x, y)

    # Element-wise addition
    def vec_add(self, pos, direction):
        return tuple(map(sum, zip(pos, direction)))

    # Check surroundings for a connecting pipe, return the first found
    def find_first(self, pos):
        # peek in any direction
        for direction in [N, E, S, W]:
            pipe_pos = self.vec_add(pos, direction)
            pipe_symbol = self.map[pipe_pos]
            for connection in ctrl[pipe_symbol]:
                # We found a symbol that has a connection to us!
                if pos == self.vec_add(pipe_pos, connection):
                    return pipe_pos

    # Start walking from S into the first found direction until back to S
    def walk(self):
        path = []
        path.append(self.find_start())
        path.append(self.find_first(path[0]))
        i = 1
        while self.map[path[i]] != 'S':
            for connection in ctrl[self.map[path[i]]]:
                candidate = self.vec_add(path[i], connection)
                # If the next position is not our origin, it must be our
                # destination
                if candidate != path[i-1]:
                    path.append(candidate)
            i += 1
        self.pipe_path = path
        self.pipe_length = i

pm = PipeMap()
# print(pm)
# print(pm.find_first(pm.find_start()))
pm.walk()
print(pm.pipe_length//2)
