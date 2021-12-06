import re
from math import sqrt
from itertools import chain

# 1

with open("input.txt") as f:
    lines = [[int(x) for x in re.split(r" -> |,", x.strip())] for x in f]

    matrix_size = max(chain(*lines)) + 1
    mat = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    for (x1, y1, x2, y2) in lines:
        if x1 != x2 and y1 != y2:
            continue
        length = int(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        dir = None
        if x2 > x1:
            dir = "right"
        elif x2 < x1:
            dir = "left"
        elif y2 > y1:
            dir = "down"
        elif y2 < y1:
            dir = "up"
        for i in range(length + 1):
            if dir == "right":
                mat[y1][x1 + i] += 1
            elif dir == "left":
                mat[y1][x1 - i] += 1
            elif dir == "up":
                mat[y1 - i][x1] += 1
            elif dir == "down":
                mat[y1 + i][x1] += 1
            else:
                raise Error("Wrong")
    print("1: {}".format(sum(1 for x in chain(*mat) if x > 1)))


# 2
import re
from math import sqrt
from itertools import chain


# 2

with open("input.txt") as f:
    lines = [[int(x) for x in re.split(r" -> |,", x.strip())] for x in f]

    matrix_size = max(chain(*lines)) + 1
    mat = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    for (x1, y1, x2, y2) in lines:
        length = max(abs(x2 - x1), abs(y2 - y1))
        dir = None
        if x2 > x1 and y1 == y2:
            dir = "east"
        elif x2 < x1 and y1 == y2:
            dir = "west"
        elif y2 > y1 and x1 == x2:
            dir = "south"
        elif y2 < y1 and x1 == x2:
            dir = "north"
        elif x2 > x1 and y2 > y1:
            dir = "southeast"
        elif x2 < x1 and y2 > y1:
            dir = "southwest"
        elif x2 > x1 and y2 < y1:
            dir = "northeast"
        elif x2 < x1 and y2 < y1:
            dir = "northwest"
        for i in range(length + 1):
            if dir == "east":
                mat[y1][x1 + i] += 1
            elif dir == "west":
                mat[y1][x1 - i] += 1
            elif dir == "north":
                mat[y1 - i][x1] += 1
            elif dir == "south":
                mat[y1 + i][x1] += 1
            elif dir == "northeast":
                mat[y1 - i][x1 + i] += 1
            elif dir == "northwest":
                mat[y1 - i][x1 - i] += 1
            elif dir == "southeast":
                mat[y1 + i][x1 + i] += 1
            elif dir == "southwest":
                mat[y1 + i][x1 - i] += 1
    print("2: {}".format(sum(1 for x in chain(*mat) if x > 1)))
