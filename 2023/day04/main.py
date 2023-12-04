import re
from collections import defaultdict


with open("input.txt") as f:
    p1 = 0
    p2 = defaultdict(int)
    for i, line in enumerate(f):
        (answer, mine) = [
            set(re.findall(r"(\d+)[^:\d]", segment)) for segment in line.split("|")
        ]
        wins = len(set.intersection(answer, mine))
        p1 += int(2 ** (wins - 1))
        p2[i] += 1
        for j in range(wins):
            p2[i + j + 1] += p2[i]

    print("1:", p1)
    print("2:", sum(p2.values()))
