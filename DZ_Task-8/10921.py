from itertools import *

cnt = 0
for val in set(permutations('джаваскрипт')):
    val = ''.join(val)
    if (val.index('а') + 1) + (val.index('и') + 1) + (val.index('а', val.index('а') + 1) + 1) == 11:
        cnt += 1
print(cnt)

# 604800