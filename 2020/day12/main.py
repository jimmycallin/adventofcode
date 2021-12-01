# 1

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


# 2

with open("input.txt") as f:
    instructions = [(x[0], int(x.strip()[1:])) for x in f.readlines()]

    origo = [0, 0]
    current = list(origo)
    waypoint = [10, 1]
    for action, value in instructions:
        if action == "F":
            current = [c + value * w for c, w in zip(current, waypoint)]
        elif action == "N":
            waypoint[1] += value
        elif action == "E":
            waypoint[0] += value
        elif action == "W":
            waypoint[0] -= value
        elif action == "S":
            waypoint[1] -= value
        elif action in ["R", "L"]:
            n_turns = value // 90
            direction = 1 if action == "R" else -1
            for _ in range(n_turns):
                new_waypoint = [0, 0]
                new_waypoint[0] = waypoint[1] * direction
                new_waypoint[1] = -waypoint[0] * direction
                waypoint = new_waypoint

    print("2:", abs(current[0]) + abs(current[1]))