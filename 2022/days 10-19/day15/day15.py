import time


class Sensor:
    def __init__(self, sensPos: tuple[int, int], bacPos: tuple[int, int]) -> None:
        self.a = sensPos[0]
        self.b = sensPos[1]
        self.r = self.radius(bacPos)

    def inNeighborhood(self, pos: tuple[int, int]) -> bool:
        return abs(pos[0]-self.a) + abs(pos[1]-self.b) <= self.r

    def intersectLine(self, y: int) -> int:
        return self.r - abs(y-self.b)

    def radius(self, pos: tuple[int, int]) -> int:
        return abs(pos[0]-self.a) + abs(pos[1]-self.b)

    def __eq__(self, s: object) -> bool:
        return self.a == s.a and self.b == s.b


def yes(input: list[str]) -> tuple[list[Sensor], set[tuple[int, int]]]:
    sens = []
    bacons = set()
    for line in input:
        line = line.split(': closest beacon is at x=')
        posS = line[0].split('x=')[1].split(', y=')
        posB = line[1].split(', y=')
        s = Sensor((int(posS[0]), int(posS[1])), (int(posB[0]), int(posB[1])))
        sens.append(s)
        bacons.add((int(posB[0]), int(posB[1])))

    return sens, bacons


def checkIntersection(x: int, y: int, sensors) -> bool:
    """If current position is in a circle of at least one of sensors return False.
    Else return true -> that is the seeking Bacon."""
    s1: Sensor
    for s1 in sensors:
        if s1.inNeighborhood((x, y)):
            return False
    return True


def first(sensors: list[Sensor], bacons: set[tuple[int, int]], y: int) -> None:
    """Go through each sensor and check how far away from y=2000000 it is (that
    is, only by vertical component. Then generate range of i's that each
    sensor intersects. (m = radius - b) => distance from ceter of sensor to line y.
    Number of elements that is intersects is (2*m + 1), these are centered
    at (x = a). This works nicely because Manhattan distance produces
    'circles' around S."""
    x = set()
    s: Sensor
    for s in sensors:
        m = s.intersectLine(y)
        if m >= 0:
            x.update([i for i in range(s.a - m, s.a + m+1)])

    for b in bacons:
        if b[1] == y:
            x.remove(b[0])
    print(len(x))


def second(sensors: list[Sensor], lim: int) -> None:
    """Circle around the edge of each sensor. Still takes ~ 8 sec.

    Optimization idea: instead of circling around sensors, circle around Beacons. In that case
    you should save bacons as type Sensor as well (problem: radius = (manhattan dis to closest B)//2)."""
    x, y = 0, 0
    for s in sensors:
        u, v = 1, -1
        # start one up and one left from the far left side of sensor
        x, y = s.a-(s.r+1) + u, s.b + v
        foundTheBitch = False
        # end when reaching far left side of sensor or when finding B
        while x != s.a-(s.r+1) or y != s.b:
            if x >= 0 and x <= lim and y >= 0 and y <= lim:
                if checkIntersection(x, y, sensors):
                    foundTheBitch = True
                    break

            if x == s.a and y == s.b-(s.r+1):
                u, v = 1, 1
            elif x == s.a+(s.r+1) and y == s.b:
                u, v = -1, 1
            elif x == s.a and y == s.b+(s.r+1):
                u, v = -1, -1

            x, y = x+u, y+v

        if foundTheBitch:
            break

    print(x * lim + y)


if __name__ == "__main__":
    start = time.time()
    with open('in.txt') as f:
        input = f.read().splitlines()

    sensors, bacons = yes(input)

    # first(sensors, bacons, 2000000)
    second(sensors, 4000000)

    end = time.time()
    print(end-start)
