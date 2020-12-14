import re

# 1

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    mask = ""
    mem = {}
    for line in lines:
        if line.startswith("mask"):
            mask = re.search(r"mask = (\w+)$", line.strip())[1]
        if line.startswith("mem"):
            groups = re.search(r"mem\[(\d+)\] = (\d+)$", line.strip())
            mem_addr, mem_value = int(groups[1]), bin(int(groups[2]))[2:]
            padded_mem_value = list('0' * (len(mask) - len(mem_value)) + mem_value)
            for i, mask_val in enumerate(mask):
                if mask_val == "X":
                    continue
                else:
                    padded_mem_value[i] = mask_val
            mem[mem_addr] = int("".join(padded_mem_value), 2)
    print("1:", sum(mem.values()))


# 2

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    mask = ""
    mem = {}
    for line in lines:
        if line.startswith("mask"):
            mask = re.search(r"mask = (\w+)$", line.strip())[1]
        if line.startswith("mem"):
            groups = re.search(r"mem\[(\d+)\] = (\d+)$", line.strip())
            mem_addr, mem_value = int(groups[1]), bin(int(groups[2]))[2:]
            padded_mem_value = list('0' * (len(mask) - len(mem_value)) + mem_value)
            for i, mask_val in enumerate(mask):
                if mask_val == "X":
                    continue
                else:
                    padded_mem_value[i] = mask_val
            mem[mem_addr] = int("".join(padded_mem_value), 2)
    print("2:", sum(mem.values()))
