# 1


def get_adj_dir(seats, i, j, dir_y, dir_x):
    if dir_y == -1 and i == 0:
        return None
    if dir_x == -1 and j == 0:
        return None
    if dir_y == 1 and i >= len(seats) - 1:
        return None
    if dir_x == 1 and j >= len(seats[i]) - 1:
        return None

    curr = "."
    while curr == ".":
        i = i + dir_y
        j = j + dir_x
        if i >= 0 and i < len(seats) and j >= 0 and j < len(seats[i]):
            curr = seats[i][j]
        else:
            curr = None
    return curr


def get_adjacents(seats, i, j):
    t_l = get_adj_dir(seats, i, j, -1, -1)
    t = get_adj_dir(seats, i, j, -1, 0)
    t_r = get_adj_dir(seats, i, j, -1, 1)
    l = get_adj_dir(seats, i, j, 0, -1)
    r = get_adj_dir(seats, i, j, 0, 1)
    b_l = get_adj_dir(seats, i, j, 1, -1)
    b = get_adj_dir(seats, i, j, 1, 0)
    b_r = get_adj_dir(seats, i, j, 1, 1)
    return (t_l, t, t_r, l, r, b_l, b, b_r)


def next_state(seats, i, j):
    curr = seats[i][j]

    if curr == "#":
        adjacents = get_adjacents(seats, i, j)
        n_free = sum(1 for x in adjacents if x == "#")
        if n_free >= 5:
            return "L"
        return curr
    if curr == "L":
        adjacents = get_adjacents(seats, i, j)
        n_occupied = sum(1 for x in adjacents if x == "#")
        if n_occupied == 0:
            return "#"
        return curr
    return curr


def print_seats(seats):
    for i in seats:
        print(i)


def is_equal(seats, next_state):
    eq = []
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == next_state[i][j]:
                eq.append(True)
            else:
                eq.append(False)
    return all(eq)


def n_occupied(seats):
    occupied = 0
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == "#":
                occupied += 1
    return occupied


with open("input.txt") as f:
    prev_state_seats = [list(x.strip()) for x in f.readlines()]
    next_state_seats = [list(x) for x in prev_state_seats]

    n_rounds = 0

    while n_rounds == 0 or not is_equal(prev_state_seats, next_state_seats):
        n_rounds += 1
        prev_state_seats = [list(x) for x in next_state_seats]
        for i in range(len(prev_state_seats)):
            for j in range(len(prev_state_seats[i])):
                next_state_seats[i][j] = next_state(prev_state_seats, i, j)
        # print("---")
        # print_seats(next_state_seats)
    print("2:", n_occupied(next_state_seats))
