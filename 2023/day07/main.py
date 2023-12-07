import re

# 1

FIVE_OAK = 1000000000000
FOUR_OAK = 100000000000
FULL_HOUSE = 10000000000
THREE_OAK = 1000000000
TWO_PAIRS = 100000000
ONE_PAIR = 10000000
HIGH = 1000000


def order_score(cards, ordering):
    return (
        14**4 * ordering[cards[0]]
        + 14**3 * ordering[cards[1]]
        + 14**2 * ordering[cards[2]]
        + 14**1 * ordering[cards[3]]
        + 14**0 * ordering[cards[4]]
    )


def occurrences(card, cards):
    return len(re.findall(card[0], cards))


with open("input.txt") as f:
    order1 = {
        y: x
        for x, y in enumerate(
            reversed(("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"))
        )
    }

    def score1(cards):
        uniqs = sorted(
            list(set(cards)), key=lambda c: occurrences(c, cards), reverse=True
        )

        if occurrences(uniqs[0], cards) == 5:
            return FIVE_OAK + order_score(cards, order1)
        if occurrences(uniqs[0], cards) == 4:
            return FOUR_OAK + order_score(cards, order1)
        if occurrences(uniqs[0], cards) == 3 and occurrences(uniqs[1], cards) == 2:
            return FULL_HOUSE + order_score(cards, order1)
        if occurrences(uniqs[0], cards) == 3:
            return THREE_OAK + order_score(cards, order1)
        if occurrences(uniqs[0], cards) == 2 and occurrences(uniqs[1], cards) == 2:
            return TWO_PAIRS + order_score(cards, order1)
        if occurrences(uniqs[0], cards) == 2:
            return ONE_PAIR + order_score(cards, order1)
        return HIGH + order1[uniqs[0]] + order_score(cards, order1)

    ranked = [
        (rank + 1, bid)
        for rank, (_, bid) in enumerate(
            sorted(
                [
                    (score1(hand), int(bid))
                    for (hand, bid) in (line.strip().split() for line in f.readlines())
                ],
                key=lambda x: x[0],
            )
        )
    ]

    print("1:", sum(x[0] * x[1] for x in ranked))


# 2


with open("input.txt") as f:
    order2 = {
        y: x
        for x, y in enumerate(
            reversed(("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"))
        )
    }

    def score2(cards):
        uniqs = sorted(
            list(set(cards)),
            key=lambda c: occurrences(c, cards) + order2[c] / 100,
            reverse=True,
        )
        highest = uniqs[0] if uniqs[0] != "J" else uniqs[1] if len(uniqs) > 1 else "A"
        jokered = cards.replace("J", highest)
        if occurrences(highest, jokered) == 5:
            return FIVE_OAK + order_score(cards, order2)
        if occurrences(highest, jokered) == 4:
            return FOUR_OAK + order_score(cards, order2)
        if occurrences(highest, jokered) == 3 and occurrences(uniqs[1], jokered) == 2:
            return FULL_HOUSE + order_score(cards, order2)
        if occurrences(highest, jokered) == 3:
            return THREE_OAK + order_score(cards, order2)
        if occurrences(highest, jokered) == 2 and occurrences(uniqs[1], jokered) == 2:
            return TWO_PAIRS + order_score(cards, order2)
        if occurrences(highest, jokered) == 2:
            return ONE_PAIR + order_score(cards, order2)
        return HIGH + order2[highest] + order_score(cards, order2)

    ranked = [
        (rank + 1, bid)
        for rank, (_, bid) in enumerate(
            sorted(
                [
                    (score2(hand), int(bid))
                    for (hand, bid) in (line.strip().split() for line in f.readlines())
                ],
                key=lambda x: x[0],
            )
        )
    ]
    print("2:", sum(x[0] * x[1] for x in ranked))
