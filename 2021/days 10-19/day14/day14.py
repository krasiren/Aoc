def readIn(input):
    temp = input[0]
    dic = {}
    for line in input[2:]:
        p = line.split(' -> ')
        dic.update({p[0]: p[1]})

    return temp, dic


def first(dic: dict, temp: str) -> None:
    for i in range(3):
        next = ''
        for j in range(len(temp)-1):
            next += temp[j] + dic[temp[j:j+2]]

        temp = next + temp[-1]
        print(temp)

    count = [0 for i in range(ord('A'), ord('Z')+1)]
    for x in temp:
        count[ord(x) - ord('A')] += 1

    min, max = len(temp), 0
    for i, a in enumerate(count):
        if a != 0:
            if a < min:
                min = a
            if a > max:
                max = a

    print(max - min)


if __name__ == "__main__":
    with open('ex.txt') as f:
        input = f.read().splitlines()

    temp, dic = readIn(input)

    first(dic, temp)

    print()
