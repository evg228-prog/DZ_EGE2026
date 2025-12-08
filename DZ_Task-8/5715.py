from itertools import *

cnt = 0
for p, b, k in product(range(16), repeat=3):
    if k > p > b and k + p + b <= 15:
        cnt += 1
print(cnt)

# 102