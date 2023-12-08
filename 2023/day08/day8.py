if __name__ == "__main__":
    with open("in.txt") as f:
        lines = f.readlines()

    instr = lines[0][:-1]
    maps = {l[:3]: (l[7:10], l[12:15]) for l in lines[2:]}

    # counts steps to one of the ends
    def countSteps(start: str, end: list[str]):
        pos = start
        i, c = 0, 0
        while pos not in end:
            if i == len(instr):
                i = 0
            if instr[i] == "L":
                pos = maps[pos][0]
            else:
                pos = maps[pos][1]
            i += 1
            c += 1

        return c

    # greatest common divisor
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    # least common multiple
    def lcm(a, b):
        return (a // gcd(a, b)) * b

    # ---- part 1 ----
    print(countSteps("AAA", ["ZZZ"]))

    # ---- part 2 ----
    pos = [e for e in maps.keys() if e.endswith("A")]
    end = [e for e in maps.keys() if e.endswith("Z")]
    steps = 1
    for p in pos:
        steps = lcm(countSteps(p, end), steps)

    print(steps)
