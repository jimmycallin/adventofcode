with open("input.txt") as f:
    instructions = [(x[0], int(x.strip()[1:])) for x in f.readlines()]

    origo = [0, 0]
    direction = (1, 0)
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    current = list(origo)
    for action, value in instructions:
        if action == "F":
            current = [c + d * value for c, d in zip(current, direction)]
        elif action == "N":
            current[1] += value
        elif action == "E":
            current[0] += value
        elif action == "W":
            current[0] -= value
        elif action == "S":
            current[1] -= value
        elif action in ["R", "L"]:
            n_turns = value // 90
            turn_dir = 1 if action == "R" else -1
            direction = directions[
                (directions.index(direction) + turn_dir * n_turns) % len(directions)
            ]
    print("1:", abs(current[0]) + abs(current[1]))
