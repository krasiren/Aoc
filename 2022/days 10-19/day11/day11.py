class Monke:
    def __init__(self, items: list[int], op, cond: bool, t: int, f: int) -> None:
        self.items = items
        self.op = op
        self.mod = cond
        self.yesM = t
        self.noM = f


def makeFunc(op: str):
    def f(x: int) -> int:
        return eval(op.replace('old', str(x)))
    return f


def makeMonkes(input: str) -> list[Monke]:
    mokes = []
    monkeys = input.split('\n\n')
    for monk in monkeys:
        atr = monk.split('\n')[1:]

        stIt = atr[0].split(':')[1].split(',')
        items = []
        for i in range(len(stIt)):
            items.append(int(stIt[i]))

        op = atr[1].split('=')[1]
        f = makeFunc(op)

        mod = int(atr[2].split('by')[1])
        tr = int(atr[3].split('monkey')[1])
        fl = int(atr[4].split('monkey')[1])

        mokes.append(Monke(items, f, mod, tr, fl))

    return mokes


def getCommon(monkes: list[Monke]) -> int:
    d = 1
    for m in monkes:
        d *= m.mod
    return d


def doRounds(monkes: list[Monke], rounds: int, div: bool) -> list[int]:
    """Because the condition at each monke is tested as a remainder of division
    with a number, we can just multiply all unique prime numbers, that make up
    all of these numbers. In my input these numbers are already primes so we
    just multiply them at part 2, then save 'new' as remainder of dividing
    with that product. Otherwise the problem at the second part is that we
    multiply with realy big numbers, and that takes...a while. Trust

    We also cannot just divide like in the first part, because that changes the
    number, hence changes the remainder, therefore we get wrong answers.

    TLDR: when making a new number (by sum or mul) try to find its 'equal'
    value in the group of primes of monke tests. That number will be reasonably
    small then."""
    monkCounts = [0] * len(monkes)
    divisor = (3 if div else getCommon(monkes))
    for _ in range(rounds):
        for monk in monkes:
            for x in monk.items:
                monkCounts[monkes.index(monk)] += 1
                y = monk.op(x)
                if div:
                    y = y // divisor
                else:
                    y = y % divisor
                if y % monk.mod == 0:
                    monkes[monk.yesM].items.append(y)
                else:
                    monkes[monk.noM].items.append(y)
            monk.items.clear()

    monkCounts.sort(reverse=True)
    return monkCounts


def first(monkes: list[Monke]) -> None:
    monkCounts = doRounds(monkes, 20, True)
    print(monkCounts, monkCounts[0] * monkCounts[1])


def second(monkes: list[Monke]) -> None:
    monkCounts = doRounds(monkes, 10000, False)
    print(monkCounts, monkCounts[0] * monkCounts[1])


if __name__ == "__main__":
    with open('in.txt') as f:
        input = f.read()

    mnkos = makeMonkes(input)

    first(mnkos)
    second(mnkos)
