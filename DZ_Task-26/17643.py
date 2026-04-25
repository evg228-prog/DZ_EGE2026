with open(r'.\files\26_17643.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: -x[1])

middle_price = sum(i[1] for i in data) / N

exp = {}
for art, price, stat in data:
    if price > middle_price:
        if art not in exp:
            exp[art] = [price, 0, 0]
        if stat == 0:
            exp[art][1] += 1
        else:
            exp[art][2] += 1

leader = None
for art in exp:
    if leader is None:
        leader = art
    elif exp[art][1] > exp[leader][1]:
        leader = art
    elif exp[art][1] == exp[leader][1] and exp[art][0] > exp[leader][0]:
        leader = art
    elif exp[art][1] == exp[leader][1] and exp[art][0] == exp[leader][0] and exp[art][2] < exp[leader][1]:
        leader = art
print(exp[leader][0] * exp[leader][1], exp[leader][2])

# 43656 36



