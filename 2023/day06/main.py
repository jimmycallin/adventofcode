import re
from functools import reduce
import math

# 1

with open("input.txt") as f:

    def get_distance(t, p):
        return (t - p) * p

    times = [int(x) for x in re.findall(r"\d+", f.readline())]
    distances = [int(x) for x in re.findall(r"\d+", f.readline())]
    ways = []
    for time, record_distance in zip(times, distances):
        way = 0
        for t in range(time):
            distance = get_distance(time, t)
            if distance > record_distance:
                way += 1
        ways.append(way)
    print("1:", reduce(lambda x, y: x * y, ways))


# 2

with open("input.txt") as f:
    time = int("".join(x for x in re.findall(r"\d+", f.readline())))
    record_distance = int("".join(x for x in re.findall(r"\d+", f.readline())))

    push_time_equals_start = math.ceil(
        (time - math.sqrt(time**2 - 4 * record_distance)) / 2
    )
    push_time_equals_end = math.ceil(
        (time + math.sqrt(time**2 - 4 * record_distance)) / 2
    )

    print("2:", push_time_equals_end - push_time_equals_start)
