# Day 10: Pipe Maze https://adventofcode.com/2023/day/10
from pathlib import Path
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

field, loop = [], []
neighOffsets = {"|": ((1, 0), (-1, 0)),
                "-": ((0, 1), (0, -1)),
                "L": ((-1, 0), (0, 1)),
                "J": ((-1, 0), (0, -1)),
                "7": ((1, 0), (0, -1)),
                "F": ((1, 0), (0, 1))}
# toNorth, toSouth, toWest, toEast
dirs = (set("|LJ"), set("|7F"), set("-J7"), set("-LF"))
with open(inputFile) as input:
    potentialS = set("|-LJ7F")
    for row in input:
        extendedRow = "." + row.strip() + "."
        if not field:
            field.append("." * len(extendedRow))
        field.append(extendedRow)       
        if not loop and "S" in extendedRow:
            loop.append((len(field) - 1, extendedRow.index("S")))
        elif len(loop) == 1:
            SRow = len(field) - 2
            SCol = field[-2].index("S")
            offsets = neighOffsets["|"] + neighOffsets["-"]
            for offset, dirIndex in zip(offsets, range(len(dirs))):
                newRow, newCol = SRow + offset[0], SCol + offset[1]
                if field[newRow][newCol] in dirs[dirIndex]:
                    loop.append((newRow, newCol))
                    potentialS &= dirs[dirIndex ^ 1]
    field.append(field[0])
    field[loop[0][0]] = field[loop[0][0]].replace("S", potentialS.pop())
    loop[0], loop[1] = loop[1], loop[0]

while loop[-1] != loop[0]:
    currRow, currCol = loop[-1]
    offsets = neighOffsets[field[currRow][currCol]]
    if (newPipe := (currRow + offsets[0][0], currCol + offsets[0][1])) != loop[-2]:
        loop.append(newPipe)
    else:
        loop.append((currRow + offsets[1][0], currCol + offsets[1][1]))
print("Part 1:", len(loop) // 2)

enclosedTiles = 0
loop = set(loop)
for idRow in range(1, len(field) - 1):
    isEnclosed = False
    for idCol in range(1, len(field[1]) - 1):
        if (idRow, idCol) in loop and field[idRow][idCol] in dirs[0]:
            isEnclosed = not isEnclosed
        elif isEnclosed and (idRow, idCol) not in loop:
            enclosedTiles += 1
print("Part 2:", enclosedTiles)