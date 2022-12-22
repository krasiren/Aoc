import time
import numpy as np

rocks = {0: np.array([[1, 1, 1, 1]]),
         1: np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
         2: np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]]),
         3: np.array([[1], [1], [1], [1]]),
         4: np.array([[1, 1], [1, 1]])}


def validMove(x, y, rock, arr) -> bool:
    if (x < 0) or (x + len(rock[0]) > len(arr[0])):
        return False
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if rock[i, j] and arr[i+y, j+x]:
                return False
    return True


def tetris(jets: list[int], limit: int) -> int:
    chamber = np.array([[0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1]])
    push = 0
    h = 0

    cutted = 0

    for i in range(limit):
        curRock = rocks[i % len(rocks)]

        if h + 4 + len(curRock) > len(chamber)+cutted:
            chamber = np.vstack(([[0]*len(chamber[0])
                                  for _ in range(len(curRock)+3)], chamber))

        # upper left corner of rock
        x, y = 2, len(chamber)+cutted - (h + 4 + len(curRock))

        while True:
            dx = jets[push % len(jets)]
            push += 1
            if validMove(x + dx, y, curRock, chamber):
                x += dx
            if validMove(x, y + 1, curRock, chamber):
                y += 1
            else:
                break
        chamber[y:y+len(curRock), x:x+len(curRock[0])] += curRock
        h = max(h, len(chamber)+cutted - 1 - y)

        if 0 not in chamber[y]:
            cutted = len(chamber) - y - 1
            chamber = chamber[:y+1]

    return h


def first(jets: list[int]) -> None:
    print(tetris(jets, 2022))


def second(jets: list[int]) -> None:
    print(tetris(jets, 1000000000000))


if __name__ == "__main__":
    with open('aoc\\2022\\days 10-19\\day17\\in.txt') as f:
        input = f.read()

    jets = [ord(c)-61 for c in input]   # (< 60), (> 61) => (< -1), (> 1)

    start = time.time()
    first(jets)
    # second(jets)

    end = time.time()
    # x = np.array([[3, 5, 7]])
    # y = np.array([5, 7])

    # x = np.vstack(([[0]*len(x[0]) for _ in range(2)], x))
    # print(x)
    # x[2:3, 0:2] = y
    print((end-start)/60)
