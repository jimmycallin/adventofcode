from collections import defaultdict
from functools import reduce

# 1

with open("input.txt") as f:
    numberlines = ([int(y) for y in x.split()] for x in f.readlines())
    diffss = []
    for numberline in numberlines:
        for numbers in numberline:
            prev = None
            diff = None
            diffs = []
            for number in numberline:
                if prev is not None:
                    diffs.append(number - prev)
                prev = number
        if diffs[0] == 0:
            continue
        elif (
            diffs[0] < 0
            and all(-4 < x < 0 for x in diffs)
            or diffs[0] > 0
            and all(4 > x > 0 for x in diffs)
        ):
            diffss.append(diffs)

    print("Ans 1:", len(diffss))


with open("input.txt") as f:
    numberlines = ([int(y) for y in x.split()] for x in f.readlines())
    ans2 = []
    for numberline in numberlines:
        for skipi, _ in enumerate(numberline):
            skipnumbers = numberline[:skipi] + numberline[skipi + 1 :]
            found = False
            if found:
                break

            prev = None
            diff = None
            diffs = []
            for number in skipnumbers:
                if prev is not None:
                    diffs.append(number - prev)
                prev = number

            if diffs[0] == 0:
                continue
            elif (
                diffs[0] < 0
                and all(-4 < x < 0 for x in diffs)
                or diffs[0] > 0
                and all(4 > x > 0 for x in diffs)
            ):
                ans2.append(diffs)
                found = True
                break

    print("Ans 2:", len(ans2))
