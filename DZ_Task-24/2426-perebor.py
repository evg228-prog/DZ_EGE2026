with open(r'.\files\24_2426.txt') as file:
    data = file.readline()

ans = 0
cnt = 0
for char in data:
    if char in '123':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)

# 20
