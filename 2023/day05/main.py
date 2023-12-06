from collections import defaultdict


class rangedict(dict):
    def __init__(self):
        super(dict)

    def get_ranges(self, source_intervals):
        intervals = []
        for (source_start, source_end), value in self.items():
            inner_intervals = []
            while source_intervals:
                (interval_start, interval_end) = source_intervals.pop()
                before = (interval_start, min(interval_end, source_start))
                intersection = (
                    max(interval_start, source_start),
                    min(source_end, interval_end),
                )
                after = (max(source_end, interval_start), interval_end)
                if before[1] > before[0]:
                    inner_intervals.append(before)
                if intersection[1] > intersection[0]:
                    intervals.append(
                        (
                            intersection[0] - source_start + value,
                            intersection[1] - source_start + value,
                        )
                    )
                if after[1] > after[0]:
                    inner_intervals.append(after)
            source_intervals = inner_intervals
        return intervals + source_intervals

    def __getitem__(self, key):
        for (start, end), val in self.items():
            if key >= start and key < end:
                return val + (key - start)
        else:
            return key


with open("input.txt") as f:
    seeds = list(map(int, f.readline().strip().split()[1:]))
    source_maps = defaultdict(rangedict)
    for line in f:
        if line.strip().endswith("map:"):
            map_name = line.split(" ")[0]
            while True:
                try:
                    nums = next(f)
                    if nums.strip() == "":
                        break
                except:
                    break
                (
                    destination_range_start,
                    source_range_start,
                    range_length,
                ) = map(int, nums.strip().split())

                source_maps[map_name][
                    (source_range_start, source_range_start + range_length)
                ] = destination_range_start

    p1 = []
    for seed in seeds:
        val = seed
        for mapname, mapping in source_maps.items():
            val = mapping[val]
        p1.append(val)
    print("1:", min(p1))

    p2 = []
    for seed_start, seed_range in list(zip(seeds[::2], seeds[1::2])):
        val = [(seed_start, seed_start + seed_range)]
        for mapname, mapping in source_maps.items():
            val = mapping.get_ranges(val)
        p2.append(min(val)[0])

    print("2: ", min(val)[0])
