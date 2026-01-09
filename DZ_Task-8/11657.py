from itertools import *
from string import *

cnt = 0
for val in product(printable[:8], repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        if '3' not in val and len(set(val)) == len(val):
            for i in '0246': val = val.replace(i, '*')
            if '**' in val:
                cnt += 1
print(cnt)

# 3852