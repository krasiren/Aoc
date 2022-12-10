from copy import deepcopy

def topCrates(stacks):
    topCr = ''
    for x in stacks[1:]:
        topCr += x.pop()
    return topCr

def first(inputLines, stacks):
    for line in inputLines:
        words = line.split(' ')
        # move 'n' from 'a' to 'b'
        n, a, b = int(words[1]), int(words[3]), int(words[5])
        for i in range(n):
            crate = stacks[a].pop()
            stacks[b].append(crate)

    print(topCrates(stacks))


def second(inputLines, stacks):
    for line in inputLines:
        words = line.split(' ')
        # move 'n' from 'a' to 'b'
        n, a, b = int(words[1]), int(words[3]), int(words[5])
        crates = stacks[a][-n:]
        del stacks[a][-n:]
        stacks[b].extend(crates)

    print(topCrates(stacks))    


if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()
    lines = lines[10:]  # delete first 10 lines

    # cuz we hardcode that monstrosity
    init_stacks = [
        [],
        ['R', 'S', 'L', 'F', 'Q'],
        ['N', 'Z', 'Q', 'G', 'P', 'T'],
        ['S', 'M', 'Q', 'B'],
        ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'],
        ['P', 'H', 'M', 'B', 'N', 'F', 'S'],
        ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'],
        ['W', 'C', 'F'],
        ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'],
        ['G', 'Z', 'D', 'L', 'C', 'N', 'R']
    ]

    l1 = deepcopy(init_stacks)
    l2 = deepcopy(init_stacks)

    first(lines, l1)
    second(lines, l2)