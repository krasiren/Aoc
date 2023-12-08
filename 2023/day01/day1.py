import numpy as np


if __name__ == "__main__":
    with open("in.txt") as f:
        lines = f.readlines()

    # part 1
    print(
        sum(
            [
                int(
                    "".join(
                        (
                            [i for i in line if i.isdigit()][0],
                            [i for i in line if i.isdigit()][-1],
                        )
                    )
                )
                for line in lines
            ]
        )
    )

    # part 2
    replacedLines = []
    for line in lines:
        newStr = ""
        for ix in range(len(line)):
            if line[ix].isdigit():
                newStr += line[ix]
            elif line.startswith("one", ix):
                newStr += "1"
            elif line.startswith("two", ix):
                newStr += "2"
            elif line.startswith("three", ix):
                newStr += "3"
            elif line.startswith("four", ix):
                newStr += "4"
            elif line.startswith("five", ix):
                newStr += "5"
            elif line.startswith("six", ix):
                newStr += "6"
            elif line.startswith("seven", ix):
                newStr += "7"
            elif line.startswith("eight", ix):
                newStr += "8"
            elif line.startswith("nine", ix):
                newStr += "9"
        replacedLines.append(newStr)

    print(replacedLines[:3])

    print(
        [
            sum(
                int(
                    "".join(
                        (
                            line[0],
                            line[-1],
                        )
                    )
                )
                for line in replacedLines
            )
        ]
    )
