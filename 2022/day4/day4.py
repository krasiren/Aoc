def makeSets(rangePairAsString):
    a1, b1 = rangePairAsString[0].split('-')
    a1, b1 = int(a1), int(b1)

    a2, b2 = rangePairAsString[1].split('-')
    a2, b2 = int(a2), int(b2)

    set1 = set(range(a1, b1+1))
    set2 = set(range(a2, b2+1))

    return set1, set2

def first(inputLines):
    count = 0

    for line in inputLines:
        pair = line.split(',')
        
        elf1, elf2 = makeSets(pair)

        if (elf1.issubset(elf2) or elf2.issubset(elf1)):
            count += 1

    print(count)

def second(inputLines):
    count = 0

    for line in inputLines:
        pair = line.split(',')

        elf1, elf2 = makeSets(pair)

        if (elf1.intersection(elf2) != set()):
            count += 1

    print(count)


if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    first(lines)
    second(lines)