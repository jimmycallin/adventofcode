import re

# 1

print(
    "1:",
    sum(
        int(x) * int(y)
        for x, y in re.findall(
            r"mul\((\d+),(\d+)\)", open("input.txt").read().replace("\n", "")
        )
    ),
)

print(
    "2:",
    sum(
        int(x) * int(y)
        for x, y in re.findall(
            r"mul\((\d{1,3}),(\d{1,3})\)",
            re.sub(
                r"don't\(\).*?do\(\)",
                "-",
                open("input.txt").read().replace("\n", "") + "do()",
            ),
        )
    ),
)
