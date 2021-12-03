from functools import reduce

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
