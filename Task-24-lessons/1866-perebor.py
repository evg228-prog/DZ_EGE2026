with open('files/24_1866.txt') as file:
    data = file.readline()

ans = 0
cnt = 1
for i in range(len(data) - 1):
    if data[i] + data[i+1] not in 'ad da':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

print(ans)

# 2252