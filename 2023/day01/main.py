import re

# 1

with open("input.txt") as f:
    lines = f.readlines()
    ans = sum(
        int(re.search(r"\d", line)[0] + re.search(r"\d", line[::-1])[0])
        for line in lines
    )
    print("1:", ans)

# 2
with open("input.txt") as f:
    numbers = "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine"
    m = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    lines = []
    for line in f.readlines():
        match = re.search(numbers, line)[0] if re.search(numbers, line) else None
        if match:
            line = line.replace(match, m[match] if match in m else match, 1)
        line = line[::-1]
        numbers = numbers[::-1]
        match = re.search(numbers, line)[0] if re.search(numbers, line) else None
        if match:
            line = line.replace(match, m[match[::-1]] if match[::-1] in m else match, 1)
        line = line[::-1]
        numbers = numbers[::-1]
        lines.append(line)
    ans = sum(
        int(re.search(r"\d", line)[0] + re.search(r"\d", line[::-1])[0])
        for line in lines
    )
    print("2:", ans)
