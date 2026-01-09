from string import *
from itertools import *

cnt = 0
for val in product(printable[:16], repeat=3):
    val = ''.join(val)
    if val[0] != '0':
        if all(val[i] > val[i + 1] for i in range(2)):
            cnt += 1
for val in product(printable[:16], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if all(val[i] > val[i + 1] for i in range(4)):
            cnt += 1
print(cnt)

# 4928
