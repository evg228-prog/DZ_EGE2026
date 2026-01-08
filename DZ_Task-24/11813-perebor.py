with open(r'.\files\24_11813.txt') as file:
    data = file.readline()

ans = 1
cnt = 1
vow = 'EYUIOA'

for i in range(len(data) - 1):
    if data[i] in vow and data[i + 1] not in vow:
        cnt += 1
    elif data[i] not in vow and data[i + 1] in vow:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(ans)

# 25