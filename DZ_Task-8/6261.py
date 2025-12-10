from itertools import *
from string import printable

cnt = 0
for val in product(printable[:8], repeat=10):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 5:
        val = val.replace('1', '*')
        val = val.replace('3', '*')
        val = val.replace('5', '*')
        if '7*' not in val and '*7' not in val and '77' not in val and '*7*' not in val:
            cnt += 1
print(cnt)

# 5888