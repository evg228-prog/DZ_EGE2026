from math import *

with open(r'.\files\16375.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 1, 1, 2]:
        rep = [i for i in set(line) if line.count(i) > 1]
        non_rep = sorted([i for i in set(line) if line.count(i) == 1])
        if prod(non_rep[:3]) > rep[0] ** 2:
            ans += 1
print(ans)

# 293