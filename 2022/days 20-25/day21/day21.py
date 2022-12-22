from sympy import symbols, solve

with open('aoc\\2022\\days 20-25\\day21\\in.txt') as f:
    input = f.read().splitlines()

monks = {}
for line in input:
    l = line.split(' ')
    m = l[0][:4]
    if len(l) == 2:
        n = int(l[1])
    else:
        n = (l[1], l[3], l[2])  # (a, b, operation)
    monks[m] = n


def yell(monke):
    if type(monks[monke]) == int:
        return monks[monke]
    if monks[monke][2] == '+':
        return yell(monks[monke][0]) + yell(monks[monke][1])
    if monks[monke][2] == '-':
        return yell(monks[monke][0]) - yell(monks[monke][1])
    if monks[monke][2] == '*':
        return yell(monks[monke][0]) * yell(monks[monke][1])
    if monks[monke][2] == '/':
        return yell(monks[monke][0]) / yell(monks[monke][1])


print(yell('root'))


def yell2(monke):
    if monke == 'root':
        return solve(yell2(monks[monke][0]) - yell2(monks[monke][1]))
    if monke == 'humn':
        return symbols('x')
    if type(monks[monke]) == int:
        return monks[monke]
    if monks[monke][2] == '+':
        return (yell2(monks[monke][0]) + yell2(monks[monke][1]))
    if monks[monke][2] == '-':
        return (yell2(monks[monke][0]) - yell2(monks[monke][1]))
    if monks[monke][2] == '*':
        return (yell2(monks[monke][0]) * yell2(monks[monke][1]))
    if monks[monke][2] == '/':
        return (yell2(monks[monke][0]) / yell2(monks[monke][1]))


monks['humn'] = 'x'
print(yell2('root'))
