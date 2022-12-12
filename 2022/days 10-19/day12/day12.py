import time


class Node:
    def __init__(self, parent=None, position=None) -> None:
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self) -> str:
        return str(self.position)


def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)


def initMatrix(input: list[str]) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    """Converts input lines into matrix with values 0-25. It also saves where S
    and E were, before it turned them to 0 and 25 correspondingly."""
    start = find('S', input)
    end = find('E', input)
    input[start[0]] = input[start[0]].replace('S', 'a')
    input[end[0]] = input[end[0]].replace('E', 'z')
    matrix = []
    for line in input:
        cur = []
        for el in line:
            cur.append(ord(el)-97)
        matrix.append(cur)

    return matrix, start, end


def direc(s: tuple[int, int], p: tuple[int, int]) -> str:
    """just for visualization of the path"""
    x1, y1 = s[0], s[1]
    x2, y2 = p[0], p[1]
    if x1 < x2:
        return 'U'
    elif x1 > x2:
        return 'D'
    elif y1 < y2:
        return 'L'
    elif y1 > y2:
        return 'R'


def writePath(steps: list[tuple[int, int]]) -> None:
    """just for visualisation of the path"""
    prev = steps[0]
    s = ''
    for step in steps:
        if step != prev:
            s += (direc(step, prev))
            prev = step
    c = 1
    t = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c += 1
        else:
            t += str(c) + s[i] + ' '
            c = 1
    t += str(c) + s[-1] + ' '
    print(t)


def allPossible(m: list[list[int]]) -> list[tuple[int, int]]:
    # coordinates of all 'b's, then we add 1 to 'count' (cheating tho)
    b = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                b.append((i, j))
    return b


def findPath(start: Node, end: Node, m: list[list[int]]) -> int:
    """A* without heuristic => Node.h = 0, so it's basically dijsktra.
    Wanted to do A* but the 'h' must contain some cost of the path to E and
    cost of the path to the next possible elevation.

    If you just uncomment bellow we get first norm of the distance from
    current node to E, this does not know where the next step 'up by one' is."""
    possible = [start]
    path = []

    while len(possible) > 0:
        current = possible[0]
        ix = 0
        for index, item in enumerate(possible):
            if item.f < current.f:
                current = item
                ix = index

        possible.pop(ix)
        path.append(current)

        # if we found a path
        if current == end:
            count = 0
            c = current
            while c != start:
                count += 1
                c = c.parent
            return count

        a, b = (current.position[0], current.position[1])
        sons = []
        for pos in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            x, y = (current.position[0] + pos[0],
                    current.position[1] + pos[1])

            if x <= (len(m) - 1) and x >= 0 and y <= (len(m[0]) - 1) and y >= 0:
                if m[x][y] <= 1 + m[a][b]:
                    sons.append(Node(current, (x, y)))

        son: Node
        for son in sons:
            if son in path:
                continue

            son.g = current.g + 1
            # son.h = ((son.position[0] - end.position[0]) **
            #          2) + ((son.position[1] - end.position[1]) ** 2)
            son.h = 0
            son.f = son.g + son.h

            add = True
            if son in possible:
                for p in possible:
                    if son.g > p.g:
                        add = False
                        break
            if add:
                possible.append(son)

    # if no path was found (surely this is big enough, copium)
    return 1000000


def first(data: tuple[list[list[int]], tuple[int, int], tuple[int, int]]) -> None:
    start = Node(None, data[1])
    end = Node(None, data[2])
    m = data[0]

    pathLength = findPath(start, end, m)
    print(pathLength)


def second(data: tuple[list[list[int]], tuple[int, int], tuple[int, int]]) -> None:
    m = data[0]
    starts = allPossible(m)
    end = Node(None, data[2])

    shortest = 490
    for s in starts:
        start = Node(None, s)
        cur = findPath(start, end, m) + 1
        if cur < shortest:
            shortest = cur

    print(shortest)


if __name__ == "__main__":
    """This is not completed program, although it works. First part takes ~ 9s,
    second part about 41-times more than that. I actually left it running for
    6min. :pepeHang:"""
    start = time.time()
    with open('in.txt') as f:
        input = f.read().splitlines()

    data = initMatrix(input)

    first(data)
    second(data)

    end = time.time()
    print(end - start)
