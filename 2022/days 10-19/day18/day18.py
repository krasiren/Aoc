import time
import numpy as np


def onEdge(space, loc: list[int], val: int) -> bool:
    diff = (-1, 1)
    for dir in range(3):
        for d in diff:
            x = loc.copy()
            x[dir] += d
            if space[tuple(x)] == val:
                return True
    return False


def countEdg(space, num: int) -> int:
    """Goes through all 1's and counts neighbouring num's"""
    count = 0
    queue = [list(np.unravel_index(np.argmax(space == 1), space.shape))]
    while queue != [[0, 0, 0]]:
        while queue != []:
            a = queue.pop(0)
            diff = (-1, 1)
            if onEdge(space, a, num):
                for dir in range(3):
                    for d in diff:
                        b = a.copy()
                        b[dir] += d
                        if b not in queue:
                            if space[tuple(b)] == num:
                                count += 1
                            elif space[tuple(b)] == 1:
                                queue.append(b)
            space[tuple(a)] = 3
        queue = [list(np.unravel_index(np.argmax(space == 1), space.shape))]

    return count


def first(points) -> None:
    minP = np.min(points)
    n = np.max(points) - minP + 3
    space = np.zeros((n, n, n))
    for p in points:
        space[p[0]-minP+1, p[1]-minP+1, p[2]-minP+1] = 1

    print(countEdg(space, 0))


def second(points) -> None:
    minP = np.min(points)
    n = np.max(points) - minP + 3
    space = np.zeros((n, n, n))
    for p in points:
        space[p[0]-minP+1, p[1]-minP+1, p[2]-minP+1] = 1

    # replace outer 0's with 2's
    space[0, 0, 0] = 2
    queue = [[0, 0, 0]]
    while queue != []:
        a = queue.pop(0)
        diff = (-1, 1)
        for dir in range(3):
            for d in diff:
                b = a.copy()
                b[dir] += d
                if (all([x >= 0 for x in b])) and (all([x < n for x in b])):
                    if (space[tuple(b)] == 0) and (b not in queue):
                        space[tuple(b)] = 2
                        queue.append(b)

    # go through 1's count 2's
    print(countEdg(space, 2))


if __name__ == "__main__":
    with open('in.txt') as f:
        input = f.read().splitlines()

    points = np.array(np.array([input[i].split(',')
                      for i in range(len(input))], dtype=int))

    start = time.time()

    first(points)
    second(points)

    end = time.time()
    print(end-start)
