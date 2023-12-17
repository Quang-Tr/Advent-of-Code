# Day 14: Parabolic Reflector Dish https://adventofcode.com/2023/day/14
from pathlib import Path
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

with open(inputFile) as input:
    platform = [row.rstrip() for row in input]

def tilt(startPlf: list[str]=platform, isCycle: bool=False) -> list[str]:
    directions = ("north", "west", "south", "east") if isCycle else ("north",)
    for direction in directions:
        rotated = map("".join, zip(*startPlf)) if direction in ("north", "south") else startPlf
        isReverse = True if direction in ("north", "west") else False
        tilted = []
        for row in rotated:
            roll = ("".join(sorted(group, reverse=isReverse)) for group in row.split("#"))
            tilted.append("#".join(roll))
        startPlf = map("".join, zip(*tilted)) if direction in ("north", "south") else tilted
    return [*startPlf]

print("Part 1:", sum((len(platform) - rowID) * row.count("O") \
                     for rowID, row in enumerate(tilt())))
configs = []
repeatedPlf = platform
while True:
    config = tuple((rowID, colID) for rowID, row in enumerate(repeatedPlf) \
                                  for colID, char in enumerate(row) \
                                  if char == "O")
    if config in configs:
        repeatStart = configs.index(config)
        repeatAfter = len(configs) - repeatStart
        break
    configs.append(config)
    repeatedPlf = tilt(repeatedPlf, True)
print("Part 2:", sum(len(platform) - rowID \
                     for rowID, _ in configs[repeatStart + (10**9 - repeatStart) % repeatAfter]))

# Simple version of just part 1:
# sum1 = 0
# barricades = [0] * len(platform[0])
# for rowID, row in enumerate(platform):
#     for colID, char in enumerate(row):
#         if char == "O":
#             sum1 += len(platform) - barricades[colID]
#             barricades[colID] += 1
#         elif char == "#":
#             barricades[colID] = rowID + 1
# print("Part 1:", sum1)