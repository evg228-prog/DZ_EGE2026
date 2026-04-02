from string import *
from itertools import *

cnt = 0

for val in product(printable[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if sum(x in '345' for x in val) == 2:
            if all(val[i] != val[i + 1] for i in range(4)):
                cnt += 1
print(cnt)

# 3078