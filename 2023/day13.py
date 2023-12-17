# Day 13: Point of Incidence https://adventofcode.com/2023/day/13
from pathlib import Path
from itertools import chain
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

def checkRefl(pattern: list[str], isSmudge: bool=False, isVertRefl: bool=False) -> int:
    for slice in range(1, len(pattern)):
        start = max(0, slice * 2 - len(pattern))
        end = min(slice * 2, len(pattern))
        compare = zip(chain.from_iterable(pattern[start:slice][::-1]), \
                      chain.from_iterable(pattern[slice:end]))
        diffChars = 0
        for char1, char2 in compare:
            if char1 != char2:
                diffChars += 1
            if diffChars > 1:
                break
        else:
            if (not isSmudge and diffChars == 0) or (isSmudge and diffChars == 1):
                return slice if isVertRefl else 100 * slice
    return checkRefl([*zip(*pattern)], isSmudge, True)

sum1 = sum2 = 0
with open(inputFile) as input:
    pattern = []
    for row in input:
        if row != "\n":
            pattern.append(row.rstrip())
        if row == "\n" or row[-1] != "\n":
            sum1 += checkRefl(pattern)
            sum2 += checkRefl(pattern, True)
            pattern.clear()
print("Part 1:", sum1)
print("Part 2:", sum2)