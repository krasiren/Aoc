def first(lines: list[str]) -> None:
    sum = 0
    cycle = 1
    x = 1
    for line in lines:
        if line[0] == 'a':
            if (cycle - 20) % 40 == 0:
                sum += (cycle * x)
            cycle += 1
            x += int(line.split(' ')[1])
        if (cycle - 20) % 40 == 0:
            sum += (cycle * x)
        cycle += 1

    print(sum)


def write(cyc: int, x: int, out: str) -> tuple[str, int]:
    if cyc == 40:
        out += '\n'
        cyc = cyc - 40
    if cyc == x-1 or cyc == x or cyc == x+1:
        out += '#'
    else:
        out += '.'

    return out, cyc


def second(lines: list[str]) -> None:
    out = ''
    cycle = 0
    x = 1
    for line in lines:
        out, cycle = write(cycle, x, out)

        # if command is 'noop' skip this
        if line[0] == 'a':
            cycle += 1
            out, cycle = write(cycle, x, out)
            x += int(line.split(' ')[1])

        cycle += 1

    print(out)


if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    first(lines)
    second(lines)
