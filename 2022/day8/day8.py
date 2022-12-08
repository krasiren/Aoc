import numpy as np

def makeVisibleTreesMatrix(lines: list[str]) -> list[list[int]]:
    # len(lines) == len(lines[0]) -> True => kvadratna matrika
    n = len(lines)
    visibleTrees = np.zeros((n, n), dtype=np.uint8)

    # trees visible from left and right
    for i in range(1, n-1):
        # from left
        peakL = -1
        for j in range(n):
            treeH = int(lines[i][j])
            if treeH > peakL:
                peakL = treeH
                visibleTrees[i][j] = 1
            if peakL == 9:
                break

        # from right
        peakR = -1
        for j in range(n):
            treeH = int(lines[i][-(j+1)])
            if treeH > peakR:
                peakR = treeH
                visibleTrees[i][-(j+1)] = 1
            if peakR == peakL:
                break
    
    # trees visible from top and bottom
    for j in range(1, n-1):
        # from top
        peakU = -1
        for i in range(n):
            treeH = int(lines[i][j])
            if treeH > peakU:
                peakU = treeH
                visibleTrees[i][j] = 1
            if peakU == 9:
                break

        # from bottom
        peakD = -1
        for i in range(n):
            treeH = int(lines[-(i+1)][j])
            if treeH > peakD:
                peakD = treeH
                visibleTrees[-(i+1)][j] = 1
            if peakD == peakU:
                break

    corners = [(a, b) for a in (0, n-1) for b in (0, n-1)]
    for x, y in corners:
        visibleTrees[x, y] = 1
    return visibleTrees

def viewingDistance(lines: list[str], i: int, j: int, hor: bool, s: int) -> int:
    n = len(lines)
    ii, jj = (i+s, j) if hor else (i, j+s)
    d = 1
    while (ii != 0) & (jj != 0) & (ii != n-1) & (jj != n-1) & (lines[ii][jj] < lines[i][j]):
        d += 1
        ii, jj = (ii+s, jj) if hor else (ii, jj+s)
    return d

def makeScenicScoreMatrix(trees: list[list[int]], lines: list[str]) -> list[list[int]]:
    n = len(lines)
    scenicScores = np.ones((n, n), dtype=np.uint32)

    for i in range(1, n-1):
        for j in range(1, n-1):
            if trees[i, j]:
                directions = [(a, b) for a in (1, 0) for b in (1, -1)]
                for hor, s in directions:
                    scenicScores[i, j] *= viewingDistance(lines, i, j, hor, s)
                
    return scenicScores

def first(trees: list[list[int]]) -> None:
    print(np.sum(trees))

def second(trees: list[list[int]], lines: list[str]) -> None:
    scenicScores = makeScenicScoreMatrix(trees, lines)
    print(np.max(scenicScores))

# not the pretties code of mine but i've tried
# it's quite optimal tho (for loops in 'makeVisibleTreesMatrix')
if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    visibletrees = makeVisibleTreesMatrix(lines)

    first(visibletrees)
    second(visibletrees, lines)