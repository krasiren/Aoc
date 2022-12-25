with open('aoc\\2022\\days 20-25\\day22\\in.txt') as f:
    input = f.read()

board = input.split('\n\n')[0].splitlines()
pswd = input.split('\n\n')[1]

max = len(board[0])
for line in board:
    if len(line) > max:
        max = len(line)
for i, line in enumerate(board):
    if len(line) < max:
        board[i] += ' ' * (max - len(line))


def getFace(y, x):
    # look at picture of my cube
    if y >= 50 and y < 100:
        return 3
    if y >= 150:
        return 6
    if y < 50:
        if x < 100:
            return 1
        else:
            return 2
    if x < 50:
        return 4
    return 5


def wrap(y, x, d, cube):
    # a bit hardcoded
    if not cube:
        if d == 0:
            return y, 0, 0, 1, d
        if d == 1:
            return 0, x, 1, 0, d
        if d == 2:
            return y, len(board[y])-1, 0, -1, d
        if d == 3:
            return len(board)-1, x, -1, 0, d

    face = getFace(y, x)
    if face == 1:
        if d == 2:
            return 100 + (49 - y), 0, 0, 1, 0
        if d == 3:
            return 150 + (x - 50), 0, 0, 1, 0

    if face == 2:
        if d == 0:
            return 100 + (49 - y), 99, 0, -1, 2
        if d == 1:
            return x-50, 99, 0, -1, 2
        if d == 3:
            return 199, x-100, -1, 0, 3

    if face == 3:
        if d == 0:
            return 49, y+50, -1, 0, 3
        if d == 2:
            return 100, y-50, 1, 0, 1

    if face == 4:
        if d == 2:
            return 149 - y, 50, 0, 1, 0
        if d == 3:
            return x+50, 50, 0, 1, 0

    if face == 5:
        if d == 0:
            return 149 - y, 149, 0, -1, 2
        if d == 1:
            return x+100, 49, 0, -1, 2

    if face == 6:
        if d == 0:
            return 149, y-100, -1, 0, 3
        if d == 1:
            return 0, x+100, 1, 0, 1
        if d == 2:
            return 0, y-100, 1, 0, 1


def move(y: int, x: int, d: int, num: int, cube: bool) -> tuple[int, int]:
    if num == 0:
        return y, x, d
    if y+dirs[d][0] >= 0 and y+dirs[d][0] < len(board) and x+dirs[d][1] >= 0 and x+dirs[d][1] < len(board[y]):
        if board[y+dirs[d][0]][x+dirs[d][1]] == '.':
            return move(y+dirs[d][0], x+dirs[d][1], d, num-1, cube)
        if board[y+dirs[d][0]][x+dirs[d][1]] == '#':
            return y, x, d

    face = getFace(y, x)
    u, v, du, dv, dn = wrap(y, x, d, cube)
    while board[u][v] == ' ':
        u += du
        v += dv
    if board[u][v] == '#':
        return y, x, d
    return move(u, v, dn, num-1, cube)


dirsName = ['R', 'D', 'L', 'U']
dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
y, x = 0, 50
d = 0
i = 0
cube = False    # part1 = False, part2 = True
while i < len(pswd):
    if pswd[i] == 'R':
        d = (d+1) % 4
        i += 1
    elif pswd[i] == 'L':
        d = (d-1) % 4
        i += 1

    num = ''
    while i < len(pswd) and pswd[i].isnumeric():
        num += pswd[i]
        i += 1
    num = int(num)
    y, x, d = move(y, x, d, num, cube)

res = 1000 * (y+1) + 4 * (x+1) + d
print(res)
