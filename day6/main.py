with open("input.txt") as f:
    n_total = 0
    n_commons = 0
    group = []
    for line in f:
        if line.strip() == "":
            n_total += len(set.union(*group))
            n_commons += len(set.intersection(*group))
            group = []
            continue
        group.append(set(line.strip()))
    n_total += len(set.union(*group))
    n_commons += len(set.intersection(*group))
    print(f"1: {n_total}")
    print(f"2: {n_commons}")
