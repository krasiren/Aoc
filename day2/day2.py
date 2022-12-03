def first(inputLines):
    score = 0
    enemyChoosesA = {'X': 3, 'Y': 6, 'Z': 0}
    enemyChoosesB = {'X': 0, 'Y': 3, 'Z': 6}
    enemyChoosesC = {'X': 6, 'Y': 0, 'Z': 3}
    selectedShape = {'X': 1, 'Y': 2, 'Z': 3}

    for line in inputLines:
        if line[0] == 'A':
            score += enemyChoosesA[line[2]]
        elif line[0] == 'B':
            score += enemyChoosesB[line[2]]
        elif line[0] == 'C':
            score += enemyChoosesC[line[2]]
        score += selectedShape[line[2]]

    print(score)

def second(inputLines):
    score = 0
    enemyChoosesA = {'X': 3, 'Y': 1, 'Z': 2}
    enemyChoosesB = {'X': 1, 'Y': 2, 'Z': 3}
    enemyChoosesC = {'X': 2, 'Y': 3, 'Z': 1}

    roundEnd = {'X': 0, 'Y': 3, 'Z': 6}

    for line in inputLines:
        if line[0] == 'A':
            score += enemyChoosesA[line[2]]
        elif line[0] == 'B':
            score += enemyChoosesB[line[2]]
        elif line[0] == 'C':
            score += enemyChoosesC[line[2]]
        score += roundEnd[line[2]]

    print(score)

if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    first(lines)
    second(lines)