with open(r'.\files\26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    cans = [int(i) for i in file]

cans = sorted(cans)

train = []
best_can = 0
for pos, can in enumerate(cans):
    if sum(train) + can <= M:
        train.append(can)
    elif sum(train) - train[-1] + can <= M:
        train[-1] = can
        best_can = pos
    else:
        break
print(len(train), sum(1 for i in cans[best_can:] if i != cans[best_can]))

# 162 788