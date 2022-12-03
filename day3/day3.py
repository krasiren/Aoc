def changeToPriority(c):
    c = ord(c)
    if (c >= 97) & (c <= 122):
        return c - (97 - 1)
    else:
        return c - (65 - 27)

def first(inputLines):
    oddItems = []

    for line in lines:
        n = int(len(line)/2)
        firstHalf = line[0:n]
        secondHalf = line[n:]
        
        for i in range(n):
            if firstHalf[i] in secondHalf:
                oddItems.append(changeToPriority(firstHalf[i]))
                break

    print(sum(oddItems))


def second(inputLines):
    numGroups = int(len(inputLines)/3)
    numSameBadges = []

    inp = inputLines
    for g in range(numGroups):
        i = 3*g
        n = int(len(inp[i]))
        for j in range(n):
            letter = inp[i][j]
            if (letter in inp[i+1]) and (letter in inp[i+2]):
                numSameBadges.append(changeToPriority(letter))
                break

    print(sum(numSameBadges))


if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    first(lines)
    second(lines)