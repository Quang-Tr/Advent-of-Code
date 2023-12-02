# Day 2: Cube Conundrum
from pathlib import Path
import re
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

# Part 1 and 2
sum1 = sum2 = 0
config = {"red": 12, "green": 13, "blue": 14}
with open(inputFile) as input:
    for game in input:
        cubes = re.split(r"\W+", game)
        gameID = int(cubes[1])
        possible = True
        power = 1
        for color in config:
            if color in cubes:
                maxQuant = max(int(cubes[i - 1]) for i, c in enumerate(cubes) if c == color)
                if maxQuant > config[color]:
                    possible = False
                power *= maxQuant
            else:
                power = 0
        if possible:
            sum1 += gameID
        sum2 += power
print("Part 1:", sum1)
print("Part 2:", sum2)