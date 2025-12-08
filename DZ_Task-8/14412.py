from itertools import *
alph = sorted('алгоритм')

cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val.count('л') <= 1 and val[0] != 'р' and  val[-1] not in 'лгртм':
        cnt += 1
print(cnt)

# 75117