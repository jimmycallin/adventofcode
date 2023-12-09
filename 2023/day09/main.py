from functools import reduce


with open("input.txt") as f:
    reports = [[int(y) for y in x.strip().split()] for x in f]
    p1 = []
    p2 = []
    for report in reports:
        diffs = [report]
        while not all(diff == 0 for diff in diffs[-1]):
            diffs.append([v2 - v1 for (v1, v2) in zip(diffs[-1], diffs[-1][1:])])

        # 1
        p1.append(sum(diff[-1] for diff in diffs))

        # 2
        p2.append(
            reduce(lambda acc, diff: diff - acc, (diff[0] for diff in reversed(diffs)))
        )

    print("1:", sum(p1))
    print("2:", sum(p2))
