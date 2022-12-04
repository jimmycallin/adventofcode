from functools import reduce


with open("input.txt") as f:
    # 1
    section_pairs = [
        [
            [int(section_pair) for section_pair in sections.split("-")]
            for sections in line.strip().split(",")
        ]
        for line in f
    ]
    max_ranges = [
        max([section[1] - section[0] + 1 for section in section_pair])
        for section_pair in section_pairs
    ]

    unions = [
        reduce(
            set.union,
            [
                set(range(section_range[0], section_range[1] + 1))
                for section_range in section_pair
            ],
        )
        for section_pair in section_pairs
    ]
    # if the union of all numbers is equal to the max range of a section
    # on of them is wrapped in the other
    ans = sum(len(union) == max_range for union, max_range in zip(unions, max_ranges))
    print("1:", ans)

    # 2
    intersections = [
        reduce(
            set.intersection,
            [
                set(range(section_range[0], section_range[1] + 1))
                for section_range in section_pair
            ],
        )
        for section_pair in section_pairs
    ]

    # if the intersection of all numbers is larger than 0
    # on of them is wrapped in the other
    ans = sum(len(intersection) > 0 for intersection in intersections)
    print("2:", ans)
