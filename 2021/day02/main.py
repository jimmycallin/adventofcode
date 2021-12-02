# 1

with open("input.txt") as f:
    x = y = 0
    lines = [line.split() for line in f]
    for (direction, steps) in lines:
        if direction == "forward":
            x += int(steps)
        elif direction == "up":
            y -= int(steps)
        elif direction == "down":
            y += int(steps)
    print("1:", x * y)

# 2

with open("input.txt") as f:
    x = y = aim = 0
    lines = [line.split() for line in f]
    for (direction, steps) in lines:
        if direction == "forward":
            x += int(steps)
            y += aim * int(steps)
        elif direction == "up":
            aim -= int(steps)
        elif direction == "down":
            aim += int(steps)
    print("2:", x * y)
