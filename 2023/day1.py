# Day 1: Trebuchet?!
from pathlib import Path
import re
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

# Part 1
sum1 = 0
with open(inputFile) as input:
    for line in input:
        digits = re.findall(r"\d", line)
        sum1 += int(digits[0] + digits[-1])
print("Part 1:", sum1)

# Part 2
sum2 = 0
keys = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
spelled = dict(zip(keys, "123456789"))
with open(inputFile) as input:
    for line in input:
        firstKeyOccurrence = (len(line), "")
        for key in keys:
            if key in line and (minIndex := line.index(key)) < firstKeyOccurrence[0]:
                firstKeyOccurrence = (minIndex, key)
        if toBeReplaced := firstKeyOccurrence[1]:
            line = line.replace(toBeReplaced, spelled[toBeReplaced] + toBeReplaced[-1], 1)
        
        lastKeyOccurrence = (-1, "")
        for key in keys:
            if key in line and (maxIndex := line.rindex(key)) > lastKeyOccurrence[0]:
                lastKeyOccurrence = (maxIndex, key)
        if toBeReplaced := lastKeyOccurrence[1]:
            line = line.replace(toBeReplaced, spelled[toBeReplaced])
        
        digits = re.findall(r"\d", line)
        sum2 += int(digits[0] + digits[-1])
print("Part 2:", sum2)