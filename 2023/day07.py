# Day 7: Camel Cards https://adventofcode.com/2023/day/7
from pathlib import Path
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

hands1, hands2 = ([[] for _ in range(7)] for _ in range(2))
HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND, \
FULL_HOUSE, FOUR_OF_A_KIND, FIVE_OF_A_KIND = range(7)
def findType(cards: str, joker: bool=False) -> int:
    counts = {label: cards.count(label) for label in set(cards)}
    if joker and "J" in counts and cards != "JJJJJ":
        Js = counts.pop("J")
        counts[max(counts, key=counts.get)] += Js
    match max(counts.values()):
        case 5:
            return FIVE_OF_A_KIND
        case 4:
            return FOUR_OF_A_KIND
        case 3:
            return FULL_HOUSE if len(counts) == 2 else THREE_OF_A_KIND
        case 2:
            return TWO_PAIR if len(counts) == 3 else ONE_PAIR
        case 1:
            return HIGH_CARD

mapLabels1 = dict(zip("AKQJT98765432", "EDCBA98765432"))
mapLabels2 = mapLabels1.copy()
mapLabels2["J"] = "1"
with open(inputFile) as input:
    for hand in input:
        cards, bid = hand.split()
        hand1, hand2 = (("".join(map(mapLabels.get, cards)), int(bid)) \
                        for mapLabels in (mapLabels1, mapLabels2))
        hands1[findType(cards)].append(hand1)
        hands2[findType(cards, True)].append(hand2)
bids1, bids2 = ((item[1] for li in hands for item in sorted(li)) \
                for hands in (hands1, hands2))
sum1, sum2 = (sum(bid * (rank + 1) for rank, bid in enumerate(bids)) \
              for bids in (bids1, bids2))
print("Part 1:", sum1)
print("Part 2:", sum2)