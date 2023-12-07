# Day 6: Wait For It https://adventofcode.com/2023/day/6
from pathlib import Path
import math
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

with open(inputFile) as input:
    times, distances = (input.readline().split()[1:] for _ in range(2))
records = list(zip(*(li + ["".join(li)] for li in [times, distances])))
records = [tuple(map(int, tup)) for tup in records]
errorMargin = 1
for time, distance in records:
    # hold**2 - time*hold + distance < 0
    if (delta := time**2 - 4*distance) > 0:
        sqrtDelta = math.sqrt(delta)
        root1 = (time - sqrtDelta) / 2
        minHold = int(root1) + 1 if root1.is_integer() else math.ceil(root1)
        root2 = (time + sqrtDelta) / 2
        maxHold = int(root2) - 1 if root2.is_integer() else math.floor(root2)
        if time != records[-1][0]:
            errorMargin *= maxHold - minHold + 1
        else:
            print("Part 1:", errorMargin)
            print("Part 2:", maxHold - minHold + 1)
    else:
        errorMargin = 0