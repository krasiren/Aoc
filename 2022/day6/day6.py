def startOfMarker(str, size):
    lastCharaters = []
    for i in range(len(str)):
        if i >= size:
            tmpSet = set(lastCharaters)
            if len(tmpSet) != len(lastCharaters):
                lastCharaters.pop(0)
            else:
                return i
        lastCharaters.append(str[i])

    # if start-of-___ is the last index
    return len(str)

def first(inputLines):
    print(startOfMarker(inputLines[0], 4))

def second(inputLines):
    print(startOfMarker(inputLines[0], 14))

if __name__ == "__main__":
    with open('in.txt') as f:
        lines = f.read().splitlines()

    first(lines)
    second(lines)