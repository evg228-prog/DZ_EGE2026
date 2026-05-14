with open(r'.\files\24_8510.txt') as file:
    data = file.readline()

ans = 0
cnt = 0

for i in range(len(data) - 1):
    if data[i] in 'NOP' and data[i + 1] in 'NOP':
        cnt = 1
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)

# 57