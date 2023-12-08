import re
from math import lcm


with open("input.txt") as f:
    instructions = [0 if x == "L" else 1 for x in f.readline().strip()]
    network = {
        key: (left, right)
        for (key, left, right) in re.findall(r"(\w+) = \((\w+), (\w+)\)\n", f.read())
    }

# 1

element = "AAA"
steps = 0
while element != "ZZZ":
    for instruction in instructions:
        steps += 1
        element = network[element][instruction]
print("1:", steps)

# 2

ghosts = [x for x in network.keys() if x.endswith("A")]
steps_per_ghost = {}
for ghost in ghosts:
    steps = 0
    next_node = ghost
    while not next_node.endswith("Z"):
        for instruction in instructions:
            steps += 1
            next_node = network[next_node][instruction]
    steps_per_ghost[ghost] = steps

print("2:", lcm(*steps_per_ghost.values()))
