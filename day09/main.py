# 1

with open("input.txt") as f:
    numbers = [int(line.strip()) for line in f.readlines()]
    valid = True
    preamble_length = 25
    i = preamble_length
    curr = 0
    while valid:
        preamble = set(numbers[i - preamble_length : i])
        curr = numbers[i]
        for j in preamble:
            if curr - j in preamble:
                break
        else:
            valid = False
        i += 1
    print("1: ", curr)

    for i, number in enumerate(numbers):
        acc = number
        j = i
        contiguous = [number]
        while acc < curr:
            j += 1
            acc += numbers[j]
            contiguous.append(numbers[j])
        if acc == curr:
            print("2:", min(contiguous) + max(contiguous))
            break
