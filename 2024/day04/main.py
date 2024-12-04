import re

# 1


def get_top_diagonal(msize):
    indices = []
    y = 0
    while y <= msize:
        # 0,3-1,2-2,1-3,0
        indices.append((y, msize - y))
        y += 1
    return indices


def get_bottom_diagonal(msize):
    indices = []
    y = 0
    while y <= msize:
        # 0,3-1,2-2,1-3,0
        indices.append((msize - y, y))
        y += 1
    return indices


def get_diagonals(msize):
    indices = []
    for i in range(msize):
        indices.append(get_top_diagonal(i))
        if i != msize - 1:
            indices.append(get_bottom_diagonal(i))

    return indices


def get_horizontals(msize):
    indices = []
    for i in range(msize):
        indices.append([(i, x) for x in range(msize)])
    return indices


def rotate_90_degrees(matrix):
    # Transpose the matrix and then reverse each row
    return [list(row) for row in zip(*matrix[::-1])]


def get_letters(matrix, indices):
    return "".join([matrix[y][x] for (y, x) in indices])


with open("input.txt") as f:
    input = [x.strip() for x in f.readlines()]

    matrix = input
    msize = len(matrix[0])
    letters = []
    for _ in range(4):
        for horizontal in get_horizontals(msize):
            letters.append(get_letters(matrix, horizontal))
        for diagonal in get_diagonals(msize):
            letters.append(get_letters(matrix, diagonal))
        matrix = rotate_90_degrees(matrix)
    print("1:", len(re.findall("XMAS", "-".join(letters))))
