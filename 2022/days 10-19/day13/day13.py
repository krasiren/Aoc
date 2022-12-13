from functools import cmp_to_key


def order(a, b) -> int:
    """Recursion, that compares"""
    if type(a) == type(b) == int:
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0
    elif type(a) == type(b) == list:
        for i, j in zip(a, b):
            res = order(i, j)
            if res != 0:
                return res
        if len(a) < len(b):
            return 1
        elif len(a) > len(b):
            return -1
        else:
            return 0
    else:
        if type(a) == int:
            return order([a], b)
        else:
            return order(a, [b])


def makeList(x: str) -> list[int]:
    """Hehe, yeah boi"""
    loc = {}
    exec('x = ' + x, globals(), loc)
    return loc['x']


def first(input: str) -> None:
    sum = 0
    pairs = input.split('\n\n')
    for i, pair in enumerate(pairs):
        a, b = pair.split('\n')[0], pair.split('\n')[1]
        a, b = makeList(a), makeList(b)

        if order(a, b) == 1:
            sum += i+1

    print(sum)


def second(input: str, x, y) -> None:
    ls = [x, y]
    pairs = input.split('\n\n')
    for pair in pairs:
        a, b = pair.split('\n')[0], pair.split('\n')[1]
        ls.append(makeList(a))
        ls.append(makeList(b))

    ls = sorted(ls, key=cmp_to_key(order), reverse=True)
    i, j = ls.index(x)+1, ls.index(y)+1
    print(i * j)


if __name__ == "__main__":
    with open('in.txt') as f:
        input = f.read()

    first(input)
    second(input, [[2]], [[6]])
