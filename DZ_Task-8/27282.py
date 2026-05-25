from itertools import *

alph = '0123456789ABC'
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        for i in 'ABC': val = val.replace(i, '*')
        if val.count('0') >= 2 and '**' in val and val.count('*') == 2:
            cnt += 1
print(cnt)

# 13779