with open(r'.\files\24_20909.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data) - 1):
    cnt = 0
    cnt_AB = 0
    for j in range(i, len(data) - 1):
        if data[j] == 'A' and data[j + 1] == 'B':
            cnt_AB += 1
        if cnt_AB == 101:
            break
        cnt += 1
    if cnt_AB == 101:
        ans = max(ans, cnt)
print(ans)
