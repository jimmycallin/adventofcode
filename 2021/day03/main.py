from functools import reduce
from collections import Counter

# 1

with open("input.txt") as f:
    lines = [map(int, s.strip()) for s in f]
    total = len(lines)
    summed = reduce(
        lambda a, b: [k + i for k, i in zip(a, b)],
        lines,
    )
    gamma = int("".join([str(int(x > total // 2)) for x in summed]), 2)
    epsilon = int("".join([str(int(x < total // 2)) for x in summed]), 2)
    print("1:", gamma * epsilon)

# 2

def sorted_most_common(s):
    l = Counter(s).most_common()
    return list(sorted(l, key=lambda z: (-z[1], z[0])))

def o2(lines, position=0):
    if len(lines) == 1:
        return int(lines[0], 2)
    most_commons = dict(sorted_most_common([n[position] for n in lines]))
    if most_commons["0"] > most_commons["1"]:
        return o2([n for n in lines if n[position] == "0"], position + 1)
    return o2([n for n in lines if n[position] == "1"], position + 1)

def co2(lines, position=0):
    if len(lines) == 1:
        return int(lines[0], 2)
    most_commons = dict(sorted_most_common([n[position] for n in lines]))
    if most_commons["0"] <= most_commons["1"]:
        return co2([n for n in lines if n[position] == "0"], position + 1)
    return co2([n for n in lines if n[position] == "1"], position + 1)

with open("input.txt") as f:
    lines = [s.strip() for s in f]
    print("2:", o2(lines) * co2(lines))
