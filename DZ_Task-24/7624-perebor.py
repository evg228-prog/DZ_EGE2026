with open(r'.\files\24_7624.txt') as file:
    data = file.readline()

ans = 0
cnt = 1

for i in range(len(data) - 1):
    if data[i] in 'XYZ' and data[i + 1] in 'XYZ':
        cnt = 1
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)

# 786