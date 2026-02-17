from itertools import *

cnt = 0
for val in set(permutations('просто')):
    val = ''.join(val)
    if 'оо' not in val:
        cnt += 1
print(cnt)

# 240