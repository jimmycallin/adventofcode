import re


def first(bags, inner):
    n = 0
    for content in inner.values():
        if "shiny gold bag" in content:
            n += 1
        else:
            inner_bags = {x: bags[x] for x in content}
            if first(bags, inner_bags) > 0:
                n += 1
    return n


def second(bags, inner):
    n = 0
    for bag_type, amount in inner.items():
        n += amount * (1 + second(bags, bags[bag_type]))

    return n


with open("input.txt") as f:
    bags = {}
    for line in f:
        outer, inner = line.strip().split("contain")
        inner = {
            x[1].strip(): int(x[0])
            for x in re.findall(r"(\d+) ([a-zA-Z ]+ bag)", inner)
            if x[1].strip() not in ["", "no other bag"]
        }
        bags[outer.strip().rstrip("s")] = inner
    print("1", first(bags, bags))
    print("2", second(bags, bags["shiny gold bag"]))
