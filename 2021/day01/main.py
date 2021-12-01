# 1

with open("input.txt") as f:
    lines = [int(x) for x in f]
    print("1:", sum(y - x > 0 for (x, y) in zip(lines[:-1], lines[1:])))

# 2

with open("input.txt") as f:
    lines = [int(x) for x in f]
    sums = [x+y+z for x,y,z in zip(lines[:-2], lines[1:-1], lines[2:])]
    print("2:", sum(y - x > 0 for (x, y) in zip(sums[:-1], sums[1:])))
