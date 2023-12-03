# 1

with open("input.txt") as f:
    map = {
        (r, c): v
        for (r, c, v) in [
            (r, c, v)
            for r, line in enumerate(f.readlines())
            for c, v in enumerate(line.strip())
        ]
    }

    val = ""
    adjs = ""
    good = 0
    for (r, c), v in map.items():
        if v.isdigit():
            val += v
            adjs += "".join(
                map.get(x, "")
                for x in (
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                    (r - 1, c - 1),
                    (r - 1, c + 1),
                    (r + 1, c - 1),
                    (r + 1, c + 1),
                )
            )
        else:
            if not all(s.isdigit() or s == "." for s in adjs):
                good += int(val)
            val = ""
            adjs = []
    print("1:", good)


# 2

with open("input.txt") as f:
    map = {
        (r, c): v
        for (r, c, v) in [
            (r, c, v)
            for r, line in enumerate(f.readlines())
            for c, v in enumerate(line.strip())
        ]
    }

    val = ""
    adjs = ""
    good = 0
    found_gear = {}
    new_found_gear = []
    for (r, c), v in map.items():
        if v.isdigit():
            val += v
            for a in (
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
                (r - 1, c - 1),
                (r - 1, c + 1),
                (r + 1, c - 1),
                (r + 1, c + 1),
            ):
                if map.get(a, "") == "*":
                    new_found_gear.append(a)
        else:
            for gear in new_found_gear:
                if gear not in found_gear:
                    found_gear[gear] = set()
                if int(val) not in found_gear[gear]:
                    found_gear[gear].add(int(val))
            new_found_gear = []
            val = ""
    res = 0
    for gear, vals in found_gear.items():
        if len(vals) == 2:
            res += vals.pop() * vals.pop()
    print("2:", res)
