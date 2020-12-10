# 1

with open("input.txt") as f:
    numbers = sorted([int(line.strip()) for line in f.readlines()])
    device_adapter_rate = max(numbers) + 3
    numbers = [0] + numbers + [device_adapter_rate]
    one_jolt, three_jolt = 0, 0
    for i, number in enumerate(numbers):
        if i + 1 == len(numbers):
            break
        if abs(number - numbers[i + 1]) == 1:
            one_jolt += 1
        elif abs(number - numbers[i + 1]) == 3:
            three_jolt += 1
    print("1:", one_jolt * three_jolt)

# 2


cache = {}


def count(seq):
    if len(seq) == 1:
        return 1
    if seq in cache:
        return cache[seq]
    a, b, c = 0, 0, 0
    curr = seq[0]

    if len(seq) > 1 and seq[1] - curr <= 3:
        a = count(seq[1:])
    if len(seq) > 2 and seq[2] - curr <= 3:
        b = count(seq[2:])
    if len(seq) > 3 and seq[3] - curr <= 3:
        c = count(seq[3:])
    cache[seq] = a + b + c
    return a + b + c


with open("input.txt") as f:
    numbers = tuple(sorted([int(line.strip()) for line in f.readlines()]))
    device_adapter_rate = max(numbers) + 3
    numbers = (0,) + numbers + (device_adapter_rate,)
    n = count(numbers)
    print("2:", n)