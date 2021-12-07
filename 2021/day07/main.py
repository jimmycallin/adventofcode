# 1

with open("input.txt") as f:
    ns = sorted([int(x) for x in f.read().split(",")])
    median = ns[len(ns) // 2]
    print("1:", sum([abs(x - median) for x in ns]))

# 2


def distance(dist):
    return (dist ** 2 + dist) // 2


with open("input.txt") as f:
    ns = sorted([int(x) for x in f.read().split(",")])
    minval, maxval = ns[0], ns[-1]
    print(
        "2:",
        min((sum(distance(abs(i - x)) for x in ns) for i in range(minval, maxval))),
    )
