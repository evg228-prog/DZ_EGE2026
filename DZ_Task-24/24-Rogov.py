with open(r'.\files\24_Rogov.txt') as file:
    data = file.readline()

ans = 1
cnt = 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(ans)

# 170