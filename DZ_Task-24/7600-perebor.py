with open(r'.\files\24_7600.txt') as file:
    data = file.readline()

ans = 0
cnt = 1

for i in range(len(data) - 1):
    if data[i] in 'QRS' and data[i + 1] in 'QRS':
        cnt = 1
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)

# 544