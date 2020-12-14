# 1

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    bus_ids = min(
        (abs(int(lines[0]) % -int(x)), int(x)) for x in lines[1].split(",") if x != "x"
    )
    print("1:", bus_ids[0] * bus_ids[1])


# 2

# 17,x,13,19
# 0    2  3

# 17 % t == 0
# 13 % t == 2
# 19 % t == 3


def crt(pairs):
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * pow(b, mx-2, mx)
        total %= M
    return total

with open("input.txt") as f:
    bus_ids = [
        (int(y), x)
        for x, y in enumerate(f.readlines()[1].strip().split(","))
        if y[0] != "x"
    ]
    pairs = []
    for n, i in bus_ids:
        pairs.append((n - i, n))
    print("2:", crt(pairs))
