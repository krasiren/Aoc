import time


def moveHead(coor: tuple[int, int], d: str) -> tuple[int, int]:
    x, y = coor
    match d:
        case 'U':
            return x, y-1
        case 'D':
            return x, y+1
        case 'L':
            return x-1, y
        case 'R':
            return x+1, y


def follow(current: tuple[int, int], previous: tuple[int, int]) -> tuple[int, int]:
    xh, yh = previous
    xt, yt = current
    dx, dy = xh - xt, yh - yt
    if abs(dx) > 1 or abs(dy) > 1:
        if dx == 0:
            if dy > 0:
                return xt, yt+1
            else:
                return xt, yt-1
        elif dy == 0:
            if dx > 0:
                return xt+1, yt
            else:
                return xt-1, yt
        else:
            if dx > 0:
                if dy > 0:
                    return xt+1, yt+1
                else:
                    return xt+1, yt-1
            else:
                if dy > 0:
                    return xt-1, yt+1
                else:
                    return xt-1, yt-1
    return xt, yt


def makeMoves(lines: list[str], ropeLength: int) -> set:
    """Moves head of the rope coresponding to moves in 'lines'. Then
    saves all visited locations of rope's tail. Rope cosists of
    'ropeLength'-many knots."""
    coordsVisited = set()
    rope = []
    for i in range(ropeLength):
        rope.append((0, 0))

    for line in lines:
        move = line.split(' ')
        for i in range(int(move[1])):
            rope[0] = moveHead(rope[0], move[0])

            for j in range(1, ropeLength):
                rope[j] = follow(rope[j], rope[j-1])

            coordsVisited.add(rope[-1])

    return coordsVisited


def first(lines: list[str]) -> None:
    coordsVisited = makeMoves(lines, 2)
    print(len(coordsVisited))


def second(lines: list[str]) -> None:
    coordsVisited = makeMoves(lines, 10)
    print(len(coordsVisited))


if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    start = time.time()

    first(lines)
    second(lines)

    end = time.time()
    print(end - start)
