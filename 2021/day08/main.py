# 1

print(
    "1: ",
    sum(
        1
        for d in (s for l in open("input.txt") for s in l.split("|").pop().split())
        if len(d) in set([2, 3, 4, 7])
    ),
)

# 2
