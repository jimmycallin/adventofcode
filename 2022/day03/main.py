from functools import reduce

a = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 1
with open("input.txt") as f:
    b = sum(
        a.find(set(b[: len(b.strip()) // 2]).intersection(b[len(b) // 2 :]).pop())
        for b in f
    )
    print("1:", b)

# 2
with open("input.txt") as f:
    f = [b.strip() for b in f]
    b = sum(
        a.find(
            reduce(lambda x, y: x.intersection(y), [set(c) for c in f[i : i + 3]]).pop()
        )
        for i in range(0, len(f), 3)
    )
    print("2:", b)
