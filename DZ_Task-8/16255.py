from string import printable
from itertools import *

cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val[0] in '2468' and val[-1] not in '036' and '6' in val:
            cnt += 1
print(cnt)

# 827352
