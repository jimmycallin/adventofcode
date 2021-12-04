from functools import reduce
from collections import Counter


def transpose(matrix):
    zipped_rows = zip(*matrix)
    return [list(row) for row in zipped_rows]


class BingoCard:
    def __init__(self, name, matrix):
        self.name = str(name)
        self.matrix = matrix
        self.filled_in = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    def register(self, draw):
        for i, row in enumerate(self.matrix):
            for j, col in enumerate(row):
                if draw == col:
                    self.filled_in[i][j] = True

    def has_won(self):
        for row in self.filled_in:
            if all(row):
                return True
        for row in transpose(self.filled_in):
            if all(row):
                return True
        return False

    def final_score(self, draw):
        unmarked = []
        for i, row in enumerate(self.filled_in):
            for j, col in enumerate(row):
                if not col:
                    unmarked.append(self.matrix[i][j])
        return int(draw) * sum(map(int, unmarked))


# 1


with open("input.txt") as f:
    draws = [x.strip() for x in f.readline().split(",")]
    f.readline()
    cards = []
    for i, matrices in enumerate(f.read().split("\n\n")):
        cards.append(
            BingoCard(i, [m.strip().split() for m in matrices.strip().split("\n")])
        )

    winner = None
    winning_draw = None
    for draw in draws:
        for card in cards:
            card.register(draw)
            if card.has_won():
                winner = card
                winning_draw = draw
                break
        if winner:
            break
    print("1: ", winner.final_score(winning_draw))

# 2

with open("input.txt") as f:
    draws = [x.strip() for x in f.readline().split(",")]
    f.readline()
    cards = []
    for i, matrices in enumerate(f.read().split("\n\n")):
        cards.append(
            BingoCard(i, [m.strip().split() for m in matrices.strip().split("\n")])
        )

    winners = []
    last_winning = None
    winning_draw = None
    for draw in draws:
        for card in cards:
            if card in winners:
                continue
            card.register(draw)
            if card.has_won():
                winners.append(card)
                if len(winners) == len(cards):
                    last_winning = card
                    winning_draw = draw
                    break
        if last_winning:
            break
    print("2: ", last_winning.final_score(winning_draw))
