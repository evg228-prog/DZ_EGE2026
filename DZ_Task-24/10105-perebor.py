with open(r'.\files\24_10105.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)):
    cnt = 0
    cnt_T = 0
    for j in range(i, len(data)):
        if data[j] == 'T':
            cnt_T += 1
        if cnt_T == 101:
            break
        cnt += 1
    if cnt_T == 101:
        ans = max(ans, cnt)

print(ans)

# 133