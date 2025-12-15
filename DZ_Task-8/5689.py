from itertools import *
from string import printable

cnt = 0
for val in product(printable[:2], repeat=16):
    val = ''.join(val)
    if val[0] != '0' and sum(map(int, val)) % 3 == 0:
        cnt += 1
print(cnt)

# 10923