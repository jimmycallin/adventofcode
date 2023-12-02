import re
from functools import reduce

# 1


with open("input.txt") as f:
    maxes = {"red": 12, "green": 13, "blue": 14}
    games = []
    gameRegex = r"(\d+): (.+)$"
    for line in f:
        for match in re.findall(gameRegex, line):
            game = int(match[0])
            valids = all(
                all(
                    int(cubes) <= maxes[color]
                    for cubes, color in re.findall(r"(\d+) (\w+)", draw)
                )
                for draw in match[1].split(";")
            )
            if valids:
                games.append(game)
    print("1: ", sum(games))


# 2


with open("input.txt") as f:
    games = []
    gameRegex = r"(\d+): (.+)$"
    for line in f:
        for match in re.findall(gameRegex, line):
            game = int(match[0])
            cgroup = {"red": [], "green": [], "blue": []}
            for draw in match[1].split(";"):
                for cubes, color in re.findall(r"(\d+) (\w+)", draw):
                    cgroup[color].append(int(cubes))
            games.append(reduce(lambda x, y: x * y, (max(v) for v in cgroup.values())))
    print("2: ", sum(games))
