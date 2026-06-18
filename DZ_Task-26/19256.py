with open(r'.\files\26_19256.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(set(tuple(i) for i in data))
best_id = 0
ans = 0
cnt = 1

for i in range(len(data) - 1):
    if data[i][0] == data[i + 1][0] and data[i + 1][1] - data[i][1] == 1:
        cnt += 1
    else:
        if cnt > ans:
            ans = cnt
            best_id = data[i][0]
        elif cnt == ans and data[i][0] < best_id:
            best_id = data[i][0]
        cnt = 1
print(best_id, ans)

# 40031 148