from itertools import *

vow = 'оиа'
con = 'сртвк'
cnt = 0
for val in set(permutations('сортировка')):
    val = ''.join(val)
    for i in vow: val = val.replace(i, '*')
    for i in con: val = val.replace(i, '+')
    if '***' not in val and '+++' not in val:
        cnt += 1
print(cnt)

# 185760