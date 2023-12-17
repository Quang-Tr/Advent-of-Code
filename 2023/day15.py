# Day 15: Lens Library https://adventofcode.com/2023/day/15
from pathlib import Path
from functools import reduce
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

def hashAlgo(hashVal: int, char: str) -> int:
    return (hashVal + ord(char)) * 17 % 256

sum1 = sum2 = 0
with open(inputFile) as input:
    steps = input.readline().rstrip().split(",")
boxes = dict(zip(range(256), (([], []) for _ in range(256))))
for step in steps:
    sum1 += reduce(hashAlgo, step, 0)
    if step[-1] == "-":
        label = step[:-1]
        box = reduce(hashAlgo, label, 0)
        try:
            boxes[box][1].pop(boxes[box][0].index(label))
            boxes[box][0].remove(label)
        except ValueError:
            pass
    else:
        label, focal = step[:-2], int(step[-1])
        box = reduce(hashAlgo, label, 0)
        try:
            boxes[box][1][boxes[box][0].index(label)] = focal
        except ValueError:
            boxes[box][1].append(focal)
            boxes[box][0].append(label)
print("Part 1:", sum1)
for box, lenses in boxes.items():
    sum2 += sum((box + 1) * (slot + 1) * focal for slot, focal in enumerate(lenses[1]))
print("Part 2:", sum2)