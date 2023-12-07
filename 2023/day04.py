# Day 4: Scratchcards https://adventofcode.com/2023/day/4
from pathlib import Path
import re
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

sum1 = 0
cardNum = 0
instances = {}
with open(inputFile) as input:
    for card in input:
        win, have = (set(li.split()) for li in re.split(r":|\|", card)[1:])
        if (match := len(win & have)) > 0:
            sum1 += 2**(match - 1)
        
        cardNum += 1
        instances[cardNum] = instances.get(cardNum, 0) + 1
        for copy in range(cardNum + 1, cardNum + 1 + match):
            instances[copy] = instances.get(copy, 0) + instances[cardNum]
print("Part 1:", sum1)
print("Part 2:", sum(instances.values()))