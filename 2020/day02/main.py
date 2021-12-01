import re

# 1

with open("input.txt") as f:
    n_valids = 0
    for line in f:
        min, max, letter, input = re.split(r"[\s:-]\s?", line.strip())
        counted = input.count(letter)
        n_valids += int(min) <= counted <= int(max)
    print("VALID", n_valids)


# 2

with open("input.txt") as f:
    n_valids = 0
    for line in f:
        i1, i2, letter, input = re.split(r"[\s:-]\s?", line.strip())
        counted = (input[int(i1) - 1] + input[int(i2) - 1]).count(letter)
        n_valids += counted == 1
    print("VALID", n_valids)
