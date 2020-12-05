def get_row(line, max_row, min_row):
    if len(line) == 0:
        return min(max_row, min_row)
    if line[0] in ["F", "L"]:
        max_row = max_row - (max_row - min_row + 1) // 2
        return get_row(line[1:], max_row, min_row)
    elif line[0] in ["B", "R"]:
        min_row = min_row + (max_row - min_row + 1) // 2
        return get_row(line[1:], max_row=max_row, min_row=min_row)
    else:
        raise RuntimeError("Shouldn't get here", line)


def get_seat_id(line):
    row = line[:7]
    row_number = get_row(row, 127, 0)
    col = line[7:]
    col_number = get_row(col, 7, 0)
    return row_number * 8 + col_number


with open("input.txt") as f:
    seat_ids = []
    for line in f:
        seat_ids.append(get_seat_id(line.strip()))
    print("1: Max seat id: {}".format(max(seat_ids)))

    sorted_seats = sorted(seat_ids)
    my_seat = [
        seat_id + 1
        for idx, seat_id in enumerate(sorted_seats)
        if idx < len(sorted_seats) - 1 and sorted_seats[idx + 1] != seat_id + 1
    ][0]
    print("2: My seat is: {}".format(my_seat))