with open(r'.\files\26_20910.txt') as file:
    N, M, K = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
prew_row, prew_place = data[0]
best_row = 0
best_place = 0

for row, place in enumerate(data, start=1):
    if prew_row == row:
        if place - prew_place == 1:
            if