# 1

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    bus_ids = min(
        (abs(int(lines[0]) % -int(x)), int(x)) for x in lines[1].split(",") if x != "x"
    )
    print("1:", bus_ids[0] * bus_ids[1])
