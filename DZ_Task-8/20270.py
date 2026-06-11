from itertools import *
from string import *

cnt = 0
for val in product(printable[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0246': val = val.replace(i, '*')
        if '***' not in val and val.count('**') >= 2:
            cnt += 1
print(cnt)

# 576