from itertools import *

cnt  = 0

for val in permutations('абиколун', r=8):
    val = ''.join(val)
    for i in 'аиоу': val = val.replace(i, '*')
    for i in 'бклн': val = val.replace(i, '#')
    if '**' not in val and '##' not in val:
        cnt += 1
print(cnt)

# 1152