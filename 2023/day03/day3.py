import numpy as np


class Num:
    def __init__(self, row, startIx=None, len=None, value=None) -> None:
        self.row = row
        self.start = startIx
        self.len = len
        self.collBox = None
        self.value = value
        self.setCollBox()

    def setCollBox(self):
        self.collBox = []
        for i in range(self.len):
            self.collBox.append((self.row, self.start + i))

    def nextTo(self, x, y):
        possible = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                possible.append((x + i, y + j))
        for point in possible:
            if point in self.collBox:
                return True
        return False

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    with open("in.txt") as f:
        lines = f.readlines()

    # part 1
    notPartChars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    rowsOfNumbers = []

    # TODO: poprau to da bo s classom delal, k grdo zgleda kle
    def isPartNum(x, y, lenght):  # se for loop az vse
        # zgorna vrstica
        if x != 0:
            if y != 0:
                if lines[x - 1][y - 1] not in notPartChars:
                    return True
            if y != len(lines[0]) - 2:
                if lines[x - 1][y + 1] not in notPartChars:
                    return True
            if lines[x - 1][y] not in notPartChars:
                return True
        # spodna vrstica
        if x != len(lines) - 1:
            if y != 0:
                if lines[x + 1][y - 1] not in notPartChars:
                    return True
            if y != len(lines[0]) - 2:
                if lines[x + 1][y + 1] not in notPartChars:
                    return True
            if lines[x + 1][y] not in notPartChars:
                return True
        # v isti vrstici levo pa desno
        if y != 0:
            if lines[x][y - 1] not in notPartChars:
                return True
        if y != len(lines[0]) - 2:
            if lines[x][y + 1] not in notPartChars:
                return True

        # rekurzivno se za druge stevke pogleda
        if lenght > 1:
            return isPartNum(x, y + 1, lenght - 1)

        return False

    vsota = 0
    for i, line in enumerate(lines):
        currNum = ""
        currNumStartIx = 0
        row = []
        for j, char in enumerate(line):
            if char.isdigit():
                if currNum == "":
                    currNumStartIx = j
                currNum += char
            else:
                if currNum != "" and isPartNum(i, currNumStartIx, len(currNum)):
                    vsota += int(currNum)
                    row.append(Num(i, currNumStartIx, len(currNum), int(currNum)))
                currNum = ""
        rowsOfNumbers.append(row)
    print(f"part 1: {vsota}")

    # part 2
    def adj(x, y):
        adjNums = []
        currPossibleNums = np.append(rowsOfNumbers[x - 1], rowsOfNumbers[x])
        currPossibleNums = np.append(currPossibleNums, rowsOfNumbers[x + 1])
        for num in currPossibleNums:
            if num.nextTo(x, y) and num not in adjNums:
                adjNums.append(num)

        if len(adjNums) != 2:
            return False, False

        return adjNums[0].value, adjNums[1].value

    vsota = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "*":
                n1, n2 = adj(i, j)
                if n1 and n2:
                    vsota += n1 * n2

    print(f"part 2: {vsota}")
