with open(r'.\files\24_11241.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for i in data:
    if i in 'ABCD':
        ans = max(cnt, ans)
        cnt = 0
    else:
        cnt += 1
ans = max(cnt, ans)
print(ans)

# 193