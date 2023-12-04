# Day 3: Gear Ratios https://adventofcode.com/2023/day/3
from pathlib import Path
import re
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

numbers = []
symbols = {}
with open(inputFile) as input:
    for row in input:
        numbers.append({})
        for match in re.finditer(r"\d+", row):
            numbers[-1][match.span()] = int(match.group())
        for match in re.finditer(r"[^.\d\n]", row):
            symbols[(len(numbers) - 1, match.start())] = match.group()

sum2 = 0
adjPosNoDups = set()
for symbolPos in symbols:
    adjToStar = []
    for adjRow in range(max(0, symbolPos[0] - 1), min(symbolPos[0] + 2, len(numbers))):
        for span in numbers[adjRow]:
            if max(span[0], symbolPos[1] - 1) < min(span[1], symbolPos[1] + 2):
                adjPosNoDups.add((adjRow, span))

                if symbols[symbolPos] == "*":
                    adjToStar.append(numbers[adjRow][span])
    if len(adjToStar) == 2:
        sum2 += adjToStar[0] * adjToStar[1]
print("Part 1:", sum(numbers[row][span] for row, span in adjPosNoDups))
print("Part 2:", sum2)