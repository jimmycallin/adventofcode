transform = {"X": "A", "Y": "B", "Z": "C"}
scoring = {"A": 1, "B": 2, "C": 3}
beats = {"A": "C", "B": "A", "C": "B"}
loses = {"A": "B", "B": "C", "C": "A"}

# 1

with open("input.txt") as f:
    a = [x.strip().split(" ") for x in f]
    a = sum(
        scoring[transform[x[1]]]
        + (6 if x[0] in beats[transform[x[1]]] else 3 if x[0] == transform[x[1]] else 0)
        for x in a
    )

    print("1:", a)


# 2


def pick(a, b):
    if b == "X":
        return beats[a]
    elif b == "Y":
        return a
    elif b == "Z":
        return loses[a]


with open("input.txt") as f:
    a = [x.strip().split(" ") for x in f]
    a = sum(
        scoring[pick(*x)] + (6 if x[1] == "Z" else 3 if x[1] == "Y" else 0) for x in a
    )

    print("2:", a)
