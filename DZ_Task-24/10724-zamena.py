from string import *

with open(r'.\files\24_10724.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase[:6]

res = ''
for i in data:
    if i in alph:
        res += i
    else:
        res += ' '

data = res.split()

ans = 0
for p in data:
    if len(p) == 1:
        ans = max(ans, 1)
    elif p[0] != '0':
        ans = max(ans, len(p))

print(ans)

# Долго работает, надеюсь, что выдаст 21 :)