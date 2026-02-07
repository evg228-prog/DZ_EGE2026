with open(r'.\files\24_3792.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in data:
    if i in 'ABC':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)

# 16