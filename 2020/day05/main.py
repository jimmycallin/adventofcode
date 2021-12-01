def get_number(line, max_row, min_row):
    if len(line) == 0:
        return min_row
    elif line[0] in ["F", "L"]:
        max_row = max_row - (max_row - min_row + 1) // 2
        return get_number(line[1:], max_row, min_row)
    else:
        min_row = min_row + (max_row - min_row + 1) // 2
        return get_number(line[1:], max_row=max_row, min_row=min_row)


with open("input.txt") as f:
    seat_ids = []
    for line in f:
        row_number = get_number(line.strip()[:7], 127, 0)
        col_number = get_number(line.strip()[7:], 7, 0)
        seat_ids.append(row_number * 8 + col_number)
    seat_ids = sorted(seat_ids)

    my_seat = [
        seat_id + 1
        for idx, seat_id in enumerate(seat_ids)
        if idx < len(seat_ids) - 1 and seat_ids[idx + 1] != seat_id + 1
    ][0]

    print("1: Max seat id: {}".format(max(seat_ids)))
    print("2: My seat is: {}".format(my_seat))