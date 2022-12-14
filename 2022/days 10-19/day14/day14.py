import time
import numpy as np


def getMinMax(lines: list[str]) -> tuple[int, int, int, int]:
    xmin, ymin = 1000000, 1000000
    xmax, ymax = 0, 0
    for line in lines:
        coord = line.split(' -> ')
        x, y = [], []
        for p in coord:
            p = p.split(',')
            x.append(int(p[0]))
            y.append(int(p[1]))
        for i in x:
            if i < xmin:
                xmin = i
            if i > xmax:
                xmax = i
        for j in y:
            if j < ymin:
                ymin = j
            if j > ymax:
                ymax = j
    return xmin, xmax, ymin, ymax


def saveMatrix(m) -> None:
    """Nice visualization"""
    np.savetxt('out.txt', m, fmt='%1d')
    with open('out.txt') as f:
        arr = f.read()
    arr = arr.replace('0', ' ')
    arr = arr.replace('1', '-')
    arr = arr.replace('2', 'o')
    with open('out.txt', 'w') as f:
        f.write(arr)
        f.close()


def makeRocks(lines: list[str]) -> tuple[list[list[int]], int]:
    """Returns a matrix of size (ymax, xmax-xmin) with added zeros on 
    left and right, so 'dropSand' doesn't fall out of bounds. This is
    the smallest possible matrix (in width) from input data."""
    x1, x2, y1, y2 = getMinMax(lines)

    # horSize = (y2+2)*2 + 1    this is the minimum required horSize
    ro = np.zeros((y2+3, (y2+2)*2 + 1), dtype='uint8')

    for line in lines:
        coord = line.split(' -> ')
        x, y = [], []
        for p in coord:
            p = p.split(',')
            x.append(int(p[0]) - (500 - (y2+2)))
            y.append(int(p[1]))
        for i in range(len(x) - 1):
            a, b = (x[i], x[i+1]) if x[i] <= x[i+1] else (x[i+1], x[i])
            c, d = (y[i], y[i+1]) if y[i] <= y[i+1] else (y[i+1], y[i])
            ro[c:d+1, a:b+1] = 1

    ro[-1, :] = 1       # floor
    # uncomment to see initial matrix
    # saveMatrix(ro)
    return ro, y2+2


def falling(m, pos) -> None:
    m[pos] = 2
    saveMatrix(m)
    time.sleep(0.1)
    m[pos] = 0


def dropSand(m: list[list[int]], y: int, x: int, stop: bool) -> None:
    # uncomment to see the animation of falling sand
    # falling(m, (y, x))
    if stop and (y == len(m)-3):
        m[y, x] = 2
        return

    if m[y+1, x] == 0:
        return dropSand(m, y+1, x, stop)
    elif m[y+1, x-1] == 0:
        return dropSand(m, y+1, x-1, stop)
    elif m[y+1, x+1] == 0:
        return dropSand(m, y+1, x+1, stop)
    else:
        m[y, x] = 2
        return


def first(rocks: list[list[int]], offset: int) -> None:
    count = 0
    while 2 not in rocks[offset-2]:
        # 500 - (500 - (y2+2)) = y2+2 = 163 shhhh
        dropSand(rocks, 0, offset, True)
        count += 1
        # uncomment to see where each grain of sand stops
        # saveMatrix(rocks)
        # time.sleep(0.2)

    count -= 1
    # uncomment to see final output
    # saveMatrix(rocks)
    print(count)


def second(rocks: list[list[int]], offset: int) -> None:
    count = 0
    while rocks[0, offset] != 2:
        dropSand(rocks, 0, offset, False)
        count += 1
        # uncomment to see where each grain of sand stops
        # saveMatrix(rocks)
        # time.sleep(0.15)

    # uncomment to see final output
    # saveMatrix(rocks)
    print(count)


if __name__ == "__main__":
    """Part 1 < 1s, part 2 ~ 7s"""
    with open('in.txt') as f:
        input = f.read().splitlines()

    rocks, offset = makeRocks(input)

    start = time.time()
    first(rocks, offset)

    second(rocks, offset)
    end = time.time()

    print(end-start)
