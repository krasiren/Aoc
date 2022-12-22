class A:
    def __init__(self, val) -> None:
        self.val = val

    # def __eq__(self, __o: object) -> bool:
    #     return self.val == __o.val


with open('aoc\\2022\\days 20-25\\day20\\in.txt') as f:
    input = f.read().splitlines()

# a = [int(i) * 811589153 for i in input]
a = [A(int(x)) for x in input]
b = a.copy()
zero, = [i for i in a if i.val == 0]

# for _ in range(10): # part 2
for el in a:
    x = b.index(el)
    y = (x + el.val) % (len(a)-1)

    del b[x]
    b.insert(y, el)
    # also works
    # if y > x:
    #     b[x:y] = b[x+1:y+1]
    # elif y < x:
    #     b[y+1:x+1] = b[y:x]
    # b[y] = el

ix0 = b.index(zero)
sum = b[(1000 + ix0) % len(b)].val + b[(2000 + ix0) %
                                       len(b)].val + b[(3000 + ix0) % len(b)].val
print(sum)
