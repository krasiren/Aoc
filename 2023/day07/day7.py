class Hand:
    # ordered from strongest to weakest
    p1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    p2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def __init__(self, value, bid, joker=False) -> None:
        self.value = value
        self.bid = int(bid)
        self.joker = joker
        self.type = self.calcType()

    def calcType(self):
        prev = {}
        jC = 0
        for c in self.value:
            if self.joker and c == "J":
                jC += 1
            elif c in prev:
                prev[c] += 1
            else:
                prev[c] = 1

        counted = sorted(list(prev.values()))
        if len(counted) != 0:
            counted[-1] += jC
        else:
            counted = [5]

        if len(counted) == 1:
            return 0
        if len(counted) == 5:
            return 6
        if 4 in counted:
            return 1
        if 3 in counted and 2 in counted:
            return 2
        if 3 in counted:
            return 3
        if 2 in counted and len(counted) == 3:
            return 4
        return 5

    def __lt__(self, other):
        arr = Hand.p2 if self.joker else Hand.p1
        for i in range(len(self.value)):
            if self.value[i] != other.value[i]:
                return arr.index(self.value[i]) > arr.index(other.value[i])
        return False

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


if __name__ == "__main__":
    with open("in.txt") as f:
        lines = f.readlines()

    def getSum(partTwo: bool):
        groupedByType = {i: [] for i in reversed(range(7))}
        for line in lines:
            curr = Hand(*line.split(), joker=partTwo)
            groupedByType[curr.type].append(curr)

        rank = 1
        vsota = 0
        for t in groupedByType:
            for item in sorted(groupedByType[t]):
                vsota += rank * item.bid
                rank += 1

        return vsota

    # part 1
    print(getSum(False))
    # part 2
    print(getSum(True))
