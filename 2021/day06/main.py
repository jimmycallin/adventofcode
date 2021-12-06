import re
from math import sqrt
from itertools import chain

# 1

with open("input.txt") as f:
    lines = [int(x) for x in f.read().split(",")]
    for _ in range(1, 81):
        for i, line in enumerate(lines):
            if line > 0:
                lines[i] -= 1
            elif line == 0:
                lines[i] = 6
                lines.append(9)
    print("1:", len(lines))

# 2

cache = {}

def count(j, maxdepth):
    if (j, maxdepth) in cache:
        return cache[(j, maxdepth)]
    if maxdepth == 0:
        return 1
    if j == 0:
        res = count(6, maxdepth - 1) + count(8, maxdepth - 1)
        cache[(j, maxdepth)] = res
        return res
    else:
        return count(j - 1, maxdepth - 1)


with open("input.txt") as f:
    lines = [int(x) for x in f.read().split(",")]
    s = 0
    maxdepth = 256
    for i, line in enumerate(lines):
        s += count(line, maxdepth)
    print("2:", s)
