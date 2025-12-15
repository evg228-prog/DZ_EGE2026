from itertools import *
from string import printable

cnt = 0
for val in product('0123456789AB', repeat=7):
    if val[0] != '0' and val.count('B') == 2:
        val = ''.join(['*' if i in '13579B' else '+' for i in val])
        if val == '*+*+*+*' or val =='+*+*+*+':
            cnt += 1
print(cnt)

# 48600