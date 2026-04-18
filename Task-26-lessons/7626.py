with open(r'.\files\26_7626.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

cells = [0] * K
last_cell = 0
cnt = 0

for time in sorted(times):
    for i in range(K):
        if cells[i] < time[0]:
            cells[i] = time[1]
            cnt += 1
            last_cell = i + 1
            break
print(cnt, last_cell)

# 581 59