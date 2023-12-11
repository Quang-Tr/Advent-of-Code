# Day 11: Cosmic Expansion https://adventofcode.com/2023/day/11
from pathlib import Path
from itertools import combinations
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

galaxies = []
nonEmptyCols = set()
rowXpNums1, rowXpNums2 = [0], [0]
with open(inputFile) as input:
    rowNum = 0
    for row in input:
        start = 0
        while (colNum := row.find("#", start)) > -1:
            galaxies.append((rowNum, colNum))
            nonEmptyCols.add(colNum)
            start = colNum + 1
        if rowNum == 0:
            rowNum += 1
            continue
        if start == 0:
            rowXpNums1.append(rowXpNums1[-1] + 2)
            rowXpNums2.append(rowXpNums2[-1] + 10**6)
        else:
            rowXpNums1.append(rowXpNums1[-1] + 1)
            rowXpNums2.append(rowXpNums2[-1] + 1)
        rowNum += 1
colXpNums1, colXpNums2 = [0], [0]
for colNum in range(max(nonEmptyCols) + 1):
    if colNum == 0:
        continue
    if colNum not in nonEmptyCols:
        colXpNums1.append(colXpNums1[-1] + 2)
        colXpNums2.append(colXpNums2[-1] + 10**6)
    else:
        colXpNums1.append(colXpNums1[-1] + 1)
        colXpNums2.append(colXpNums2[-1] + 1)

sum1 = sum2 = 0
for (row1, col1), (row2, col2) in combinations(galaxies, 2):
    sum1 += abs(rowXpNums1[row1] - rowXpNums1[row2]) + abs(colXpNums1[col1] - colXpNums1[col2])
    sum2 += abs(rowXpNums2[row1] - rowXpNums2[row2]) + abs(colXpNums2[col1] - colXpNums2[col2])
print("Part 1:", sum1)
print("Part 2:", sum2)

# Straightforward but slightly slower:
# galaxies = []
# emptyRows, nonEmptyCols = set(), set()
# with open(inputFile) as input:
#     rowNum = 0
#     for row in input:
#         start = 0
#         while (colNum := row.find("#", start)) > -1:
#             galaxies.append((rowNum, colNum))
#             nonEmptyCols.add(colNum)
#             start = colNum + 1
#         if start == 0:
#             emptyRows.add(rowNum)
#         rowNum += 1
# emptyCols = set(range(min(nonEmptyCols), max(nonEmptyCols) + 1)) - nonEmptyCols

# sum1 = sum2 = 0
# for (row1, col1), (row2, col2) in combinations(galaxies, 2):
#     length = abs(row1 - row2) + abs(col1 - col2)
#     expandedRows = len(emptyRows & set(range(min(row1, row2) + 1, max(row1, row2))))
#     expandedCols = len(emptyCols & set(range(min(col1, col2) + 1, max(col1, col2))))
#     sum1 += length + expandedRows + expandedCols
#     sum2 += length + (10**6 - 1) * (expandedRows + expandedCols)
# print("Part 1:", sum1)
# print("Part 2:", sum2)