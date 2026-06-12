with open(r'.\files\26_21598.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

timeline = [0] * 1440

for time in times:
    for i in range(time[0], time[1]):
        timeline[i] += 1

ans = 0
cnt = 1
prew_change = []
for i in range(len(timeline) - 1):
    if timeline[i] == timeline[i + 1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
        prew_change.append(i + 1)

print(prew_change[-2], ans)

# 1431 13