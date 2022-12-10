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


def second(lines: list[str]) -> None:
    out = ''
    cycle = 0
    x = 1
    for line in lines:
        if cycle == 40:
            out += '\n'
            cycle = cycle - 40
        if cycle == x-1 or cycle == x or cycle == x+1:
            out += '#'
        else:
            out += '.'

        if line[0] == 'a':
            cycle += 1
            if cycle == 40:
                out += '\n'
                cycle = cycle - 40
            if cycle == x-1 or cycle == x or cycle == x+1:
                out += '#'
            else:
                out += '.'
            x += int(line.split(' ')[1])

        cycle += 1

    print(out)


if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    first(lines)
    second(lines)
