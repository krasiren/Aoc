if __name__ == "__main__":
    # AoC/2023/day05/
    with open("in.txt") as f:
        lines = f.readlines()

    # part 1
    times = [int(i) for i in lines[0].split(":")[1].split()]
    distances = [int(i) for i in lines[1].split(":")[1].split()]

    product = 1
    for i, time in enumerate(times):
        counter = 0
        for k in range(time):
            if (time - k) * k > distances[i]:
                counter += 1
        product *= counter

    print(product)

    # part 2
    time = int("".join([str(a) for a in times]))
    distance = int("".join([str(a) for a in distances]))

    lower = 0
    upper = 0

    for i in range(time):
        if (time - i) * i > distance:
            lower = i
            break

    for i in reversed(range(time)):
        if (time - i) * i > distance:
            upper = i
            break

    print(upper - lower + 1)
