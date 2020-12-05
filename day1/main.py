import itertools

with open("numbers.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]
    for a, b, c in itertools.product(lines, lines, lines):
        if a + b + c == 2020:
            print("found it {}".format(a * b * c))
            break
