if __name__ == "__main__":
    with open("in.txt") as f:
        games = f.readlines()

    # part 1
    dictLim = {"red": 12, "green": 13, "blue": 14}
    totalNum = 0
    for i, game in enumerate(games):
        possible = True
        line = game.split(":")[-1]
        sets = line.split(";")
        for set in sets:
            colors = set.split(",")

            for cubes in colors:
                for key in dictLim:
                    if key in cubes:
                        if int(cubes.strip().split(" ")[0]) > dictLim[key]:
                            possible = False
                            break

        if possible:
            totalNum += i + 1

        possible = True

    print(totalNum)

    # part 2
    vsota = 0
    for i, game in enumerate(games):
        dictMin = {"red": 0, "green": 0, "blue": 0}
        line = game.split(":")[-1]
        sets = line.split(";")
        for set in sets:
            colors = set.split(",")

            for cubes in colors:
                for key in dictMin:
                    if key in cubes:
                        dictMin[key] = max(
                            dictMin[key], int(cubes.strip().split(" ")[0])
                        )
        mult = 1
        for val in dictMin.values():
            mult *= val
        vsota += mult

    print(vsota)
