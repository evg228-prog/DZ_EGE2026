with open(r'.\files\24_18186.txt') as file:
    data = file.readline()

for i in 'AE': data = data.replace(i, '*')
for i in 'BCDFGH': data = data.replace(i, '#')

ans = []
for i in range(len(data) - 2):
    if data[i:i + 3] == '##*':
        ans.append(i)
# CCV*******CCV********CCV
res = 0
for i in range(len(ans) - 1):
    line = ans[i + 1] - ans[i] + 3
    res = max(res, line)
print(res)

# 64