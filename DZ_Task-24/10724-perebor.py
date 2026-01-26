from string import *

with open(r'.\files\24_10724.txt') as file:
    data = file.readline()

alph = digits + 'ABCDEF'
ans = 0

for i in range(len(data)):
    cnt = 0
    if data[i] in alph and data[i] != '0':
        for j in range(i, len(data)):
            if data[j] in alph:
                cnt += 1
                ans = max(ans, cnt)
            else:
                break
    elif data[i] == '0':
        ans = max(ans, cnt)
ans = max(ans, cnt)
print(ans)

# 21