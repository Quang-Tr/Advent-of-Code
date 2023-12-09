# Day 9: Mirage Maintenance https://adventofcode.com/2023/day/9
from pathlib import Path
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

sum1 = sum2 = 0
with open(inputFile) as input:
    for value in input:
        currSeq = [*map(int, value.split())]
        sum1 += currSeq[-1]
        isOddSeq = 1
        sum2 += currSeq[0]
        while len(set(currSeq)) != 1:
            currSeq = [currSeq[i + 1] - currSeq[i] for i in range(len(currSeq) - 1)]
            sum1 += currSeq[-1]
            isOddSeq = -isOddSeq
            sum2 += currSeq[0] * isOddSeq
print("Part 1:", sum1)
print("Part 2:", sum2)