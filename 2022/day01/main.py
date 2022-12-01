# 1

with open("input.txt") as f:
    ans = max(sum(int(x) for x in y.split("\n")) for y in f.read().split("\n\n"))
    print("1:", ans)

# 2
with open("input.txt") as f:
    ans = sum(sorted(sum(int(x) for x in y.split("\n")) for y in f.read().split("\n\n"))[-3:])
    print("2:", ans)