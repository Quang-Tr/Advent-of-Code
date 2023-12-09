# Day 8: Haunted Wasteland https://adventofcode.com/2023/day/8
from pathlib import Path
import re, math
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

nodes = {}
starts, ends = [], []
with open(inputFile) as input:
    instructions = tuple(map(int, input.readline().translate(str.maketrans("LR", "01", "\n"))))
    input.readline()
    for node in input:
        this, *nexts = re.findall(r"\w+", node)
        nodes[this] = nexts
        if this[-1] == "A":
            starts.append(this)
        elif this[-1] == "Z":
            ends.append(this)

def goToNextEnd(currNode: str, fromStep: int=0, endsList: list[str]=ends) -> tuple[str, int]:
    this = currNode
    currStep = fromStep
    while (next := nodes[this][instructions[currStep % len(instructions)]]) not in endsList:
        this = next
        currStep += 1
    return next, currStep + 1

steps = []
niceInput = True
for start in starts:
    correspondingEnd, stepTo1stEnd = goToNextEnd(start, endsList=["ZZZ"]) if start == "AAA" \
                                     else goToNextEnd(start)
    steps.append(stepTo1stEnd)
    if correspondingEnd == "ZZZ":
        print("Part 1:", stepTo1stEnd)
    # Optional:
    nextEnd, stepToNextEnd = goToNextEnd(correspondingEnd, stepTo1stEnd)
    if nextEnd != correspondingEnd \
       or stepToNextEnd != 2 * stepTo1stEnd or stepTo1stEnd % len(instructions) != 0:
        niceInput = False
print("Part 2:", math.lcm(*steps) if niceInput else "May the brute force be with you :)")