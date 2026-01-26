from itertools import *
from string import *

cnt = 0
for val in product(printable[:8], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and '1' not in val:
        if len(set(val)) == len(val):
            for i in '0246': val = val.replace(i, '*')
            for i in '1357': val = val.replace(i, '#')
            if '##' not in val and '**' not in val:
                cnt += 1
print(cnt)

# 180