import numpy as np

if __name__ == "__main__":
    with open("in.txt") as f:
        lines = f.readlines()

    # part 1
    vsota = 0
    for line in lines:
        nums = line.split(": ")[1]
        winning, hand = nums.split(" | ")

        winning = winning.split()
        hand = hand.split()

        n = -1
        for p in hand:
            if p in winning:
                n += 1
        vsota += 2**n if n != -1 else 0

    print(vsota)

    # part 2
    scratchcards = np.array([1 for _ in range(len(lines))])

    for i, line in enumerate(lines):
        nums = line.split(": ")[1]
        winning, hand = nums.split(" | ")

        winning = winning.split()
        hand = hand.split()

        n = 0
        for p in hand:
            if p in winning:
                n += 1
        scratchcards[i + 1 : i + n + 1] += scratchcards[i]

    print(np.sum(scratchcards))
    # print(scratchcards)
