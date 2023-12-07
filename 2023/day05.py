# Day 5: If You Give A Seed A Fertilizer https://adventofcode.com/2023/day/5
from pathlib import Path
day = Path(__file__).stem[3:]
inputFile = Path(__file__).with_name(f"input{day}.txt")

offsets = [{}]
with open(inputFile) as input:
    sources1 = [*map(int, input.readline().split()[1:])]
    sources2 = [(sources1[index], sources1[index] + sources1[index + 1]) \
                for index in range(0, len(sources1), 2)]
    for line in input:
        if line[0].isdecimal():
            dstStart, srcStart, length = map(int, line.split())
            offsets[-1][(srcStart, srcStart + length)] = dstStart - srcStart
        if line == "\n" or line[-1] != "\n":
            for index, source in enumerate(sources1):
                for span, offsetVal in offsets[-1].items():
                    if source in range(*span):
                        sources1[index] = source + offsetVal
                        break
            offsets.append({})
print("Part 1:", min(sources1))

offsets = [dict(sorted(offset.items())) for offset in offsets[1:-1]]
for offset in offsets:
    dests = []
    for srcSpan in sources2:
        toMapStart = srcSpan[0]
        for offSpan in offset:
            if offSpan[1] <= srcSpan[0]:
                continue
            if srcSpan[1] <= offSpan[0]:
                dests.append((toMapStart, srcSpan[1]))
                break
            start = max(toMapStart, offSpan[0])
            end = min(srcSpan[1], offSpan[1])
            if start != toMapStart:
                dests.append((toMapStart, start))
            dests.append((start + offset[offSpan], end + offset[offSpan]))
            if (toMapStart := end) == srcSpan[1]:
                break
        else:
            dests.append((toMapStart, srcSpan[1]))
    sources2 = dests
print("Part 2:", min(srcSpan[0] for srcSpan in sources2))