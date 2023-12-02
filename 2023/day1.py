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
        for key in keys:
            line = re.sub(key, key[0] + spelled[key] + key[-1], line)
        digits = re.findall(r"\d", line)
        sum2 += int(digits[0] + digits[-1])
print("Part 2:", sum2)