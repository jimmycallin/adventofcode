# 1

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    bus_ids = min(
        (abs(int(lines[0]) % -int(x)), int(x)) for x in lines[1].split(",") if x != "x"
    )
    print("1:", bus_ids[0] * bus_ids[1])


# 2

# 17,x,13,19
# 0    2  3

# 17 % t == 0
# 13 % t == 2
# 19 % t == 3

with open("input.txt") as f:
    bus_ids = [
        (int(y), x)
        for x, y in enumerate(f.readlines()[1].strip().split(","))
        if y[0] != "x"
    ]

    common_denominator = bus_ids[0][0]
    largest_jump = max(bus_ids)[0]
    print("largest", largest_jump)
    y = max(bus_ids)[1]
    i = 0
    found = False
    while not found:
        found = all(
            ((largest_jump * i - y) + offset) % bus_id == 0
            for bus_id, offset in bus_ids
        )
        i += 1
    print("2:", i + common_denominator)
