
# 1

with open("input.txt") as f:
    acc = 0
    visited = set()
    ops = [line.strip().split() for line in f.readlines()]
    i = 0
    while i not in visited:
        op, arg = ops[i]
        arg = int(arg)
        visited.add(i)
        if op == "nop":
            i += 1
        elif op == "acc":
            acc += arg
            i += 1
        elif op == "jmp":
            i += arg

    print("1", acc)

# 2

with open("input.txt") as f:
    changed_already = set()
    org_ops = [line.strip().split() for line in f.readlines()]
    for _ in ops:
        ops = [x for x in org_ops]
        for i, (op, arg) in enumerate(ops):
            if i in changed_already:
                continue
            if op == "nop":
                changed_already.add(i)
                ops[i] = ("jmp", arg)
                break
            elif op == "jmp":
                changed_already.add(i)
                ops[i] = ("nop", arg)
                break

        acc = 0
        visited = set()
        i = 0
        while i not in visited and i < len(ops):
            op, arg = ops[i]
            arg = int(arg)
            visited.add(i)
            if op == "nop":
                i += 1
            elif op == "acc":
                acc += arg
                i += 1
            elif op == "jmp":
                i += arg
        if i >= len(ops):
            print("2", acc)
            break
