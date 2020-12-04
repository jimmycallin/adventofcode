from functools import reduce

# 1

with open("input.txt") as f:
    grid = []
    for line in f:
        grid.append(line.strip())

x, y = 0, 0
encountered_trees = 0
while y < len(grid):
    encountered_trees += grid[y][x] == "#"
    x = (x + 3) % len(grid[y])
    y += 1
print("Task 1:")
print("Encountered trees:", encountered_trees)


# 2

print("------")
print("Task 2")
with open("input.txt") as f:
    grid = []
    for line in f:
        grid.append(line.strip())

deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
encounters = []
for (dx, dy) in deltas:
    x, y = 0, 0
    encountered_trees = 0
    while y < len(grid):
        encountered_trees += grid[y][x] == "#"
        x = (x + dx) % len(grid[y])
        y += dy
    encounters.append(encountered_trees)
print("Encountered trees:", reduce(lambda x, y: x * y, encounters, 1))
