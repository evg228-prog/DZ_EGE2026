with open(r'.\files\26_13101.txt') as file:
    N = int(file.readline())
    data = []
    for i in file:
        start, time, way = map(int, i.split())
        data.append([start, start + time, way])

data = sorted(data)
print(data)

window1 = []
window2 = []
ans_1 = 0
ans_2 = 0

for i in range(len(data)):
    cnt = 0
    if data[i][0] >= window1[-1] and (data[i][2] == 1 or data[i][2] == 0):
        if cnt < 14:
            window1[-1] = data[i][1]
            cnt += 1