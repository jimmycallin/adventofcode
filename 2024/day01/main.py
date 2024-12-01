from collections import defaultdict
from functools import reduce

# 1

with open("input.txt") as f:
    left, right = zip(
        *((int(y[0]), int(y[1])) for y in (x.split() for x in f.readlines()))
    )
    ans1 = sum((abs(x - y) for x, y in zip(sorted(left), sorted(right))))
    print("1:", ans1)

    right = reduce(
        lambda acc, y: acc.update({y: acc.get(y, 0) + 1}) or acc,
        right,
        defaultdict(int),
    )
    ans2 = sum(x * right[x] for x in left)
    print("2:", ans2)

# 2
