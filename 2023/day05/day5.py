class Range:
    def __init__(self, startIx, endIx) -> None:
        self.a = startIx
        self.b = endIx
        self.length = self.b - self.a + 1

    def overlaps(self, r):
        if self.b < r.a:
            return False
        if r.b < self.a:
            return False
        return True

    def getOverlap(self, r):
        return Range(max(self.a, r.a), min(self.b, r.b))

    def remainder(self, r):
        pass

    def remap(self, dest, source):
        return Range(dest + (self.a - source), dest + (self.b - source))

    def __str__(self) -> str:
        return f"({self.a}, {self.b}, {self.length})"


if __name__ == "__main__":
    with open("AoC/2023/day05/in.txt") as f:
        lines = f.readlines()

    seeds = [int(i) for i in lines[0].split()[1:]]
    lines = lines[2:]

    maps = {}
    novMap = True
    l = -1
    k = 0
    for line in lines:
        if novMap:
            l += 1
            maps[l] = {}
            k = 0
            novMap = False
        elif line == "\n":
            novMap = True
        else:
            maps[l][k] = [int(i) for i in line.split()]
            k += 1

    # part 1
    # minLoc = 1000000000000
    # for seed in seeds:
    #     for key in maps:
    #         for r in maps[key].values():
    #             if seed >= r[1] and seed < r[1] + r[2]:
    #                 seed = r[0] + (seed - r[1])
    #                 break

    #     if seed < minLoc:
    #         minLoc = seed
    # print(minLoc)

    # part 2
    rangeArr = []
    for i, seedStart in enumerate(seeds):
        if i % 2 == 0:
            seedsLeft = seeds[i + 1]
            rangeArr = [Range(seedStart, seedStart + seedsLeft - 1)]
            print(i)
            for key in maps:
                tempRanges = []
                for seedR in rangeArr:
                    for r in maps[key].values():
                        mapR = Range(r[1], r[1] + r[2] - 1)
                        if seedR.overlaps(mapR):
                            overlapR = seedR.getOverlap(mapR)
                            tempRanges.append(overlapR.remap(r[0], r[1]))

                            seedR = seedR.remainder(overlapR)

                        if seedR == None:
                            break

                rangeArr = tempRanges

    minLoc = 1000000000000
    for r in rangeArr:
        if r.startIx < minLoc:
            minLoc = r.startIx

    print(minLoc)
